para cambiar .py a otra carpeta:
mv 1_PYTHON_INTERNET_SOURCE.py 3.\ BASICS_from_insta.py 4.\ PLOTS_from_linkedin.py 5.\ PANDAS_VALIDATION.py ../PYTHON_FROM_WEB/

para instalar PANDAS
/usr/bin/python3 -m pip install --break-system-packages pandas numpy matplotlib seaborn wordcloud nltk statsmodels

para instalar PLOTLY
/usr/bin/python3 -m pip install --break-system-packages plotly

Explicación rápida
ModuleNotFoundError: No module named 'plotly': Ocurre porque la librería plotly no vino en el paquete de instalación anterior.
--break-system-packages: Le indica a Python 3.12 que instale plotly directamente en el entorno global (/usr/bin/python3), evitando el bloqueo PEP 668 de Ubuntu para que el kernel activo de tu ventana interactiva lo reconozca de inmediato.
Una vez que termine la descarga, vuelve a ejecutar la celda con Shift + Enter y el código funcionará correctamente.

