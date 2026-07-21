

#Si esta es la estructura para crear un OPP, ¿Cuál serían las estructuras para crear otras cosas en python?

#class Nombre):
#   def __init__(self, atributos):
#       self.atributos= atributos

#   def creo_variable(self): #f(x) llamar
#   print(f'mensaje: {self.atributo}')
#
# variable1= Nombre("s", "b", "c")
# print(Variable1.creo_variable())


# Respuesta:

#1. Estructuras de Acción: Funciones (Functional Programming)
# A veces no necesitas un objeto completo (POO), solo necesitas una transformación rápida. Esto se parece más a lo que hacías en R.

# ESTRUCTURA DE FUNCIÓN SIMPLE (Functional)
def calcular_impuesto(monto): # Definimos la acción
    return monto * 0.19 # Retornamos el cálculo

# ESTRUCTURA DE FUNCIÓN ANÓNIMA (Lambda)
# Ideal para filtros rápidos en una sola línea
limpiar_texto = lambda t: t.strip().lower() # f(x) rápida




#2. Código Comentado: Comparativa de Estructuras (Top to Down)
#He corregido los pequeños errores de sintaxis de tu ejemplo y agregado las otras formas.

# %% ESTRUCTURA 1: POO (Tu molde de clase corregido)
class Nombre: # Definimos el molde (Clase)
    def __init__(self, atributo_a, atributo_b, atributo_c): # Constructor con 3 parámetros
        self.atributo = atributo_a # Asignamos el parámetro al objeto
    
    def creo_variable(self): # Método: Acción del objeto
        return f'mensaje: {self.atributo}' # Retornamos el string formateado

# Instanciación
variable1 = Nombre("Valor A", "Valor B", "Valor C") # Creamos el objeto real
print(variable1.creo_variable()) # Imprimimos lo que devuelve el método


# %% ESTRUCTURA 2: DICCIONARIO (Estructura de Datos)
# Más rápido si no necesitas métodos, solo guardar datos
cliente_tv = { # Abrimos llaves para diccionario
    "nombre": "Canal 13", # Llave: Valor
    "rating": 45.5, # Llave: Valor
    "presupuesto": 5000 # Llave: Valor
} # Cerramos diccionario


# %% ESTRUCTURA 3: FUNCIÓN (Lógica de Procesamiento)
def procesar_tv(datos): # Recibe una estructura (como el diccionario de arriba)
    if datos["presupuesto"] > 1000: # Condicional (Decisión)
        return f"Cliente {datos['nombre']} aprobado" # Retorno de éxito
    else: # Camino alternativo
        return "Presupuesto insuficiente" # Retorno de fallo


#%%

# Ejemplo Maestro: Clase OptimizadorPro (Comentado línea a línea)
# He diseñado este ejemplo para que veas cómo todas las piezas encajan en un proceso de RegressionData.

class OptimizadorPro: # Definimos el molde del sistema avanzado
    def __init__(self, cliente, presupuesto_max): # Constructor de configuración
        self.cliente = cliente # Atributo: nombre del cliente
        self.presupuesto = presupuesto_max # Atributo: límite de gasto
        self.items_procesados = 0 # Contador de control

    def procesar_campaña(self, lista_spots): # Método que orquesta toda la lógica
        print(f"--- Iniciando proceso para {self.cliente} ---") # Log de inicio
        
        # BUCLE DEFINIDO: Recorremos cada spot de la lista
        for spot in lista_spots: # Por cada 'spot' en la colección
            
            # CONTROL DE FLUJO: 'continue'
            if spot['duracion'] <= 0: # Si el spot no tiene tiempo real
                print(f"Saltando spot {spot['id']}: Duración inválida.") # Aviso
                continue # SALTA al siguiente spot de la lista (no hace lo de abajo)

            # CONDICIONALES: 'if / elif / else'
            if spot['costo'] > self.presupuesto: # Si el costo supera el saldo
                print(f"Alerta: {spot['id']} excede el presupuesto.") # Aviso
                break # INTERRUPCIÓN: Detiene todo el proceso porque no hay más dinero
            
            elif spot['costo'] == 0: # Si el spot es un bono o gratis
                print(f"Procesando spot gratuito: {spot['id']}") # Log especial
            
            else: # Si el costo es normal y permitido
                self.presupuesto -= spot['costo'] # Restamos el costo del saldo
                self.items_processed += 1 # Aumentamos el contador
                print(f"Spot {spot['id']} aprobado. Saldo: {self.presupuesto}") # Log

        # BUCLE INDEFINIDO: 'while' para limpieza final
        while self.items_processed > 0: # Mientras queden items registrados
            print("Generando reporte parcial...") # Acción repetitiva
            self.items_processed -= 1 # Decrementamos hasta llegar a 0 (criterio de salida)
            
        print("--- Proceso Finalizado ---") # Cierre del método

        
# %%
