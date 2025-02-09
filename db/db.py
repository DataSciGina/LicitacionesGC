from pymongo import MongoClient, errors
import json
from bson import ObjectId

uri = "mongodb://mongo:dtfgRNEmgYHUFcKciMTSTYmqynIipLDD@viaduct.proxy.rlwy.net:51792"

def load_json():
    try:
        with open("data/licitaciones.json", 'r', encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
        print(f"Error al cargar JSON: {e}")
        exit()

# se define una función para los valores de _id sean cadenas (str) y no diccionarios
def clean_document(doc):
    """
    Esta función recibe los datos, convirte los valores de _id de diccionarios a cadenas (str) y retorna los datos limpios.
    """
    if isinstance(doc, dict):
        for key, value in list(doc.items()):
            if isinstance(value, dict) and "$oid" in value:
                doc[key] = ObjectId(value["$oid"])  # Convertir a ObjectId
            elif isinstance(value, dict):
                doc[key] = clean_document(value)  # Limpiar subdocumentos
            elif isinstance(value, list):
                doc[key] = [clean_document(item) if isinstance(item, dict) else item for item in value]
    return doc

def filter(data, collection):
    """Verificar y evitar duplicados antes de insertar"""
    final_docs = []
    for doc in data:
        if "_id" in doc:
            if collection.find_one({"_id": doc["_id"]}):
                print(f"Documento con _id {doc['_id']} ya existe.")
                continue  # Omitir duplicados
        final_docs.append(doc)

    return final_docs

def connect():
    """conectarse a MongoDB en Railway"""
    try:
        client = MongoClient(uri)
        db = client["licitaciones_gc"]
        collection = db["licitaciones"]
        print("Conexión exitosa a MongoDB en Railway")
    except errors.ConnectionFailure as e:
        print(f"Error de conexión: {e}")
        exit()

    data = load_json()
    
    # limpiar documentos antes de insertarlos
    clean_data = [clean_document(doc) for doc in data if isinstance(doc, dict)]
    final_data = filter(clean_data, collection)

    # insertar en MongoDB
    if final_data:
        try:
            collection.insert_many(final_data)
            print(f"{len(final_data)} documentos insertados exitosamente.")
        except errors.BulkWriteError as e:
            print(f"Error al insertar documentos: {e.details}")
    else:
        print("No hay documentos para insertar.")