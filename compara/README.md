
cd comparador
python main.py

luego, abrir: http://172.25.228.73:5000


Como nota, el PAQUETE MODULAR es:

comparador/
├── static/
│   └── styles.css      # Tu hoja de estilos
├── templates/
│   └── index.html      # La interfaz gráfica (formulario e historial)
├── main.py             # El servidor Flask y la lógica de las rutas o Código backend
└── requirements.txt    # Dependencias del proyecto o Lista de paquetes



Para transformarlo en un sitio web visual con una interfaz gráfica (HTML + CSS) y con una arquitectura modular limpia, separa la lógica del servidor de las vistas:

index.html
main.py

en template, en elindex, línea 9 se agregó esto:
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}?v=2"> 
    # Al tener ?v=2, el navegador detecta al instante que el archivo CSS cambió y lo actualiza de inmediato sin necesidad de borrar la memoria manualmente.
    Lo que permite que elpuerto después de libere y no quede atrapado.


    