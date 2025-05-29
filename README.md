# ACERIA 4C Automation Project / Proyecto de Automatización ACERIA 4C

## Overview / Resumen
This repository contains the source code for automating the operations of an ACERIA 4C, a metallurgical plant. The project is designed to monitor and manage the air flow within the system using a Flask-based backend and a simple frontend for visualization.

Este repositorio contiene el código fuente para automatizar las operaciones de una ACERIA 4C, una planta metalúrgica. El proyecto está diseñado para monitorear y gestionar el flujo de aire dentro del sistema utilizando un backend basado en Flask y un frontend simple para la visualización.

The automation system utilizes LoRaWAN for real-time data collection and stores the data in a SQLite database. Key functionalities include real-time monitoring, historical data analysis, and air volume calculation.

El sistema de automatización utiliza LoRaWAN para la recolección de datos en tiempo real y almacena los datos en una base de datos SQLite. Las funcionalidades clave incluyen monitoreo en tiempo real, análisis de datos históricos y cálculo del volumen de aire.

---

## Project Structure / Estructura del Proyecto

```
ROOT
├── BACKEND/
│   ├── app.py           # Main Flask application / Aplicación Flask principal
│   ├── lorawan.py       # LoRaWAN data simulation and management / Simulación y gestión de datos LoRaWAN
│   ├── models.py        # Database models / Modelos de base de datos
│   └── config.py        # Configuration file for environments / Archivo de configuración para entornos
├── FRONTEND/
│   ├── static/
│   │   └── scripts.js   # Frontend JavaScript for data fetching and visualization / JavaScript del frontend para obtención y visualización de datos
│   └── templates/
│       └── index.html   # Main HTML template for the frontend / Plantilla HTML principal para el frontend
└── README.md            # Project documentation / Documentación del proyecto
```

---

## Features / Características
### Backend
- **Real-time Data Fetching:** Displays the most recent flow data collected from LoRaWAN.
- **Obtención de datos en tiempo real:** Muestra los datos de flujo más recientes recolectados desde LoRaWAN.
- **Historical Data Analysis:** Allows users to query data based on specific date ranges.
- **Análisis de datos históricos:** Permite a los usuarios consultar datos basados en rangos de fechas específicos.
- **Air Volume Calculation:** Calculates total air volume consumed over a time range.
- **Cálculo del volumen de aire:** Calcula el volumen total de aire consumido en un rango de tiempo.

### Frontend
- **Dynamic Visualization:** Fetches and displays real-time and historical data.
- **Visualización dinámica:** Obtiene y muestra datos en tiempo real e históricos.
- **Simple User Interface:** Built with HTML, JavaScript, and Flask templates.
- **Interfaz de usuario simple:** Construida con HTML, JavaScript y plantillas Flask.

### LoRaWAN Integration / Integración LoRaWAN
- Simulated LoRaWAN data reception for testing and development purposes.
- Recepción simulada de datos de LoRaWAN para propósitos de prueba y desarrollo.

---

## Installation / Instalación

### Prerequisites / Requisitos previos
- Python 3.8 or later / Python 3.8 o superior
- Flask
- Flask-SQLAlchemy

### Steps / Pasos
1. Clone the repository / Clonar el repositorio:
   ```bash
   git clone https://github.com/RoxyDevs/ACERIA4C.git
   cd ACERIA4C
   ```

2. Set up a virtual environment / Configurar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Install dependencies / Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database / Inicializar la base de datos:
   ```bash
   python -c "from BACKEND.app import db; db.create_all()"
   ```

5. Run the application / Ejecutar la aplicación:
   ```bash
   python BACKEND/app.py
   ```

6. Open the application in your browser / Abrir la aplicación en tu navegador:
   ```
   http://127.0.0.1:5000/
   ```

---

## Usage / Uso

### Backend Endpoints / Endpoints del backend
- `GET /api/realtime`: Fetch the latest 10 records. / Obtiene los últimos 10 registros.
- `GET /api/historical`: Query historical data by date range (requires `start_date` and `end_date` as query parameters). / Consulta datos históricos por rango de fechas (requiere `start_date` y `end_date` como parámetros de consulta).
- `POST /api/air_volume`: Calculate air volume over a date range (requires `start_date` and `end_date` in JSON body). / Calcula el volumen de aire en un rango de fechas (requiere `start_date` y `end_date` en el cuerpo JSON).

### Frontend
The frontend is designed to interact with the backend API for real-time and historical data visualization.

El frontend está diseñado para interactuar con la API del backend para la visualización de datos en tiempo real e históricos.

- **Real-Time Data:** Automatically fetches and displays the latest 10 records. / **Datos en tiempo real:** Obtiene y muestra automáticamente los últimos 10 registros.
- **Historical Data:** Users can input a date range to query and display older records. / **Datos históricos:** Los usuarios pueden ingresar un rango de fechas para consultar y mostrar registros antiguos.

---

## Key Files / Archivos clave
### `BACKEND/app.py`
The main Flask application connects the frontend with the database and provides the RESTful API.

La aplicación Flask principal conecta el frontend con la base de datos y proporciona la API RESTful.

### `BACKEND/lorawan.py`
Simulates LoRaWAN data reception. Replace the placeholder logic with actual LoRaWAN integration for deployment.

Simula la recepción de datos LoRaWAN. Reemplaza la lógica simulada con la integración real de LoRaWAN para el despliegue.

### `BACKEND/models.py`
Defines the database schema for storing flow data.

Define el esquema de la base de datos para almacenar datos de flujo.

### `BACKEND/config.py`
Centralizes environment-specific configurations (development, testing, production).

Centraliza las configuraciones específicas del entorno (desarrollo, pruebas, producción).

---

## Future Enhancements / Mejoras Futuras
- **Deploy on Production Server:** Migrate to a production environment with WSGI server (e.g., Gunicorn).
- **Despliegue en servidor de producción:** Migrar a un entorno de producción con un servidor WSGI (por ejemplo, Gunicorn).
- **LoRaWAN Integration:** Replace the simulated data with real LoRaWAN hardware.
- **Integración LoRaWAN:** Reemplazar los datos simulados con hardware LoRaWAN real.
- **Enhanced Analytics:** Add advanced analytics and reporting features.
- **Análisis avanzado:** Agregar funciones de análisis avanzado y generación de reportes.
- **User Authentication:** Secure the application with user authentication and role-based access control.
- **Autenticación de usuarios:** Proteger la aplicación con autenticación de usuarios y control de acceso basado en roles.

---

## Contributing / Contribuciones
Contributions are welcome! Please follow these steps:

¡Las contribuciones son bienvenidas! Por favor sigue estos pasos:

1. Fork the repository. / Haz un fork del repositorio.
2. Create a new branch (`feature-name`). / Crea una nueva rama (`feature-name`).
3. Commit your changes. / Haz commit de tus cambios.
4. Push to the forked repository. / Haz push al repositorio forkeado.
5. Open a pull request. / Abre un pull request.

---

## License / Licencia
This project is licensed under the MIT License. See the `LICENSE` file for details.

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contact / Contacto
For inquiries or support, contact [RoxyDevs](https://github.com/RoxyDevs).

Para consultas o soporte, contacta a [RoxyDevs](https://github.com/RoxyDevs).
