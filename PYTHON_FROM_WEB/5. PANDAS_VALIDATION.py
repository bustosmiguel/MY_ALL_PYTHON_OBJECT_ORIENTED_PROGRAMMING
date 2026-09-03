# %%
import os
import sys

# 1. Identificar la ruta del ejecutable de Python activo
python_actual = sys.executable
print(f"=== DIAGNÓSTICO DE ENTORNO ===")
print(f"Ejecutable de Python en uso: {python_actual}")
print(f"Versión de Python: {sys.version.split()[0]}")
print(f"Directorio de trabajo: {os.getcwd()}\n")

# 2. Comprobar librerías requeridas para el script de EDA
librerias_requeridas = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "wordcloud",
    "nltk",
    "statsmodels",
]

print("=== ESTADO DE LIBRERÍAS ===")
librerias_faltantes = []

for lib in librerias_requeridas:
    try:
        __import__(lib)
        print(f"✓ {lib}: Instalado correctamente")
    except ImportError:
        print(f"✗ {lib}: NO instalado")
        librerias_faltantes.append(lib)

print("-" * 30)
if librerias_faltantes:
    print(f"Faltan instalar: {', '.join(librerias_faltantes)}")
else:
    print("Todas las librerías están listas para usarse.")


# %%

import subprocess
import sys

# Lista de librerías necesarias
paquetes = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "wordcloud",
    "nltk",
    "statsmodels",
]

print("Iniciando instalación en la ruta exacta del intérprete actual...")

# Instala directamente en la ruta del sys.executable actual
subprocess.check_call([sys.executable, "-m", "pip", "install"] + paquetes)

print("\n✓ Instalación completada. Reiniciando importaciones...")


# %%
import pandas as pd

print(f"Pandas versión {pd.__version__} cargado con éxito.")

# %%

import sys
import pandas as pd
import seaborn as sns

print(f"Ejecutable activo: {sys.executable}")
print(f"✓ Pandas versión {pd.__version__} listo.")
print(f"✓ Seaborn versión {sns.__version__} listo.")


# %%

import sys

print("Ejecutable actual:", sys.executable)
# %%
