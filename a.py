import json

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

# 1. CAPTURA DE DATOS (En la Terminal de Ubuntu)
print("--- SISTEMA DE REGISTRO REGRESSIONDATA ---")
n = input("Dígame su nombre: ")
e = input("Dígame su edad: ")
g = input("Dígame su grado: ")

# 2. CREACIÓN DEL OBJETO
estudiante = Estudiante(n, e, g)

# 3. EL PUENTE (Guardar ANTES del bucle para que Node lo vea)
datos_factura = {
    "cliente": estudiante.nombre,
    "total": estudiante.edad,
    "estado": f"Grado: {estudiante.grado} - Procesado por Python"
}

with open('data_bridge.json', 'w') as archivo:
    json.dump(datos_factura, archivo, indent=4)

print("\n✅ EXITO: Archivo data_bridge.json actualizado.")
print("🌐 Ya puedes ver los cambios en http://localhost:3000")

# 4. BUCLE DE INTERACCIÓN (Ahora sí puede quedarse aquí)
while True:
    accion = input("\nEscribe 'estudiar' o 'salir': ")
    if accion.lower() == "estudiar":
        print(f"📚 {estudiante.nombre} está estudiando...")
    elif accion.lower() == "salir":
        break