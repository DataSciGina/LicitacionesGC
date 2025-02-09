# <h1 align="center">**`Chatbot Licitaciones del Cabildo de Gran Canaria`**</h1>

<div align='center'><img src="src/img/logo-CGC.png"></div>

<h1 align='center'>Chatbot de Telegram para Consultas sobre Licitaciones del Cabildo de Gran Canaria</h1>

### Tabla de contenido

1.  [Objetivos del Proyecto](#objetivos)
2.  [Instalación y Configuración del Proyecto](#instalacion)
3.  [Proyecto Deployado](#deploy)
4.  [Stack Tecnológico](#stack)
5.  [Contacto](#contact)


<h2 align='center' id='objetivos'>Objetivos del Proyecto</h2>

Este proyecto consiste en el desarrollo de un `ChatBot` para `Telegram` que se encargará de responder preguntas específicas sobre `licitaciones del Cabildo de Gran Canaria`.

<h2 align='center' id='instalacion'>Instalacion y Configuración del Proyecto</h2>

1. **Requisitos Previos**  

Antes de comenzar, asegúrate de tener instalados los siguientes programas:
            
- [**Python**](https://www.python.org/downloads/) (versión 3.10 o superior)
- [**Node.js y npm**](https://nodejs.org/es) (versión 18.17.0, 20 o 22)
- [**Git**](https://git-scm.com/downloads) (opcional, pero recomendado)

Para verificar si ya los tienes instalados, usa:

    python --version
    node -v
    npm -v
    git --version # Opcional

2. **Crear y Activar el Entorno Virtual**

### Windows (PowerShell)

    python -m venv licitaciones_venv
    licicaciones_venv\Scripts\Activate

### Mac/Linux

    python -m venv licitaciones_venv
    source licitaciones_venv/bin/activate

3. **Instalar Dependencias**

Con el entorno virtual activado, instala las dependencias del proyecto:
    
    pip install -r requirements.txt
Si estás en Windows PowerShell y ves un error de permisos, ejecuta:
    
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

4. **Instalar y Configurar `n8n`**

Ejecuta el siguiente comando dentro del entorno virtual:

    npm install -g n8n
Si tienes problemas con npx, usa:

    & "D:\ruta\al\proyecto\licitaciones_venv\Scripts\npx.cmd" n8n

Desde el entorno virtual activado, ejecuta:

    npx n8n

Si lo estás ejecutando desde CMD en vez de PowerShell, ejecuta:

    D:\ruta\al\proyecto\licitaciones_venv\Scripts\activate.bat
    npx n8n

5. **Ejecución del Proyecto**

Para ejecutar el código principal, usa:

    python main.py
Si necesitas recargar dependencias, vuelve a ejecutar:
    
    pip install -r requirements.txt
    
6. **Solución de Problemas**

- Error `PSSecurityException` en **PowerShell**:

    Set-ExcecutionPolicy -Scope Process -ExcecutionPolicy Bypass -Force
- `npx` o `npm` no se reconocen dentro del entorno virtual:

    & "D:\ruta\al\proyecto\licitaciones_venv\Scripts\npx.cmd" n8n
- `Permisos denegados en Windows`: Ejecuta PowerShell como administrador y repite los comandos.

<h2 align='center' id='deploy'>Proyecto Deployado</h2>


<h2 align='center' id='stack'>Stack Tecnológico</h2>

- **`MongoDB:`** Para búsquedas rápidas y escalabilidad. *Alternativa:* **Google Sheet**.
- **`@BotFather:`** Para configurar el chatbot en Telegram.
- **`OpenRouter:`** Para formatear las respuestas del modelo y que se vean claras y estructuradas.
<h2 align='center' id='contact'>Contacto</h2>

<h3 align='center'><b>Agostina Fernández</b></h3>
<p align='center'>📫 fernandezagostina.ra@gmail.com</p>

<p align='center'>
    <a href="https://www.linkedin.com/in/agostina-fern%c3%a1ndez-aab4a8323/" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=13930&format=png&color=000000" alt="LinkedIn Agostina Fernández" height="40" width="40" /></a>
    <a href="https://github.com/DataSciGina" target="blank"><img align="center" src="https://img.icons8.com/?size=100&id=bVGqATNwfhYq&format=png&color=000000" alt="GitHub Agostina Fernández" height="40" width="40" /></a>
</p>