# %% ESCRITOR.PY - EL MOTOR DE DATOS
import json
import os

# Simulamos el resultado de un proceso de IA
datos_factura = {
    "cliente": "Miguel Bustos",
    "total": 10.0,
    "estado": "Procesado por Python"
}

# Guardamos los datos en un archivo JSON que Linux compartirá
with open('data_bridge.json', 'w') as archivo:
    json.dump(datos_factura, archivo, indent=4)

print("🚀 Python: Datos de factura guardados en data_bridge.json")

