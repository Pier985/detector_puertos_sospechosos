# 🛡️ Detector de Puertos Sospechosos

Este script en Python permite detectar conexiones de red activas hacia puertos comúnmente utilizados en ataques (por ejemplo, shells inversas como las de Metasploit) y registrar alertas de forma automática.

## 📌 Objetivo

Detectar conexiones sospechosas en tiempo real desde tu máquina, facilitando la labor de análisis y respuesta ante posibles intrusiones.

## ⚙️ Tecnologías utilizadas

- Python 3
- Biblioteca `psutil` para monitorizar conexiones activas
- Biblioteca `datetime` para registrar fecha y hora de las alertas

## 📂 Estructura

- `ver_conexiones.py`: Script principal que escanea conexiones activas y genera alertas.
- `alertas.log`: (se genera automáticamente) Archivo donde se registran los eventos detectados.

## 🔍 ¿Qué detecta?

El script identifica conexiones hacia puertos como:

- `4444`: común en shells reversas de Metasploit
- `5555`, `6666`, `9001`, etc.: frecuentemente usados por herramientas de ataque

Puedes personalizar la lista editando el diccionario `PUERTOS_SOSPECHOSOS` dentro del script.

## 🚀 Cómo usarlo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Pier985/detector_puertos_sospechosos.git
   cd detector_puertos_sospechosos
# detector_puertos_sospechosos
