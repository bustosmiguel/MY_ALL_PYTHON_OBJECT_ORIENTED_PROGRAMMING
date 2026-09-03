# %%


# Importamos las librerías necesarias para el análisis, generación de datos y visualización
# Importamos las librerías necesarias para el análisis, generación de datos y visualización
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import nltk
from nltk.probability import FreqDist
from statsmodels.tsa.seasonal import seasonal_decompose

# %%

# Configuración de semilla para reproducibilidad de los datos
np.random.seed(42)

# %%

# ==========================================
# CREACIÓN DEL DATASET ÚNICO
# ==========================================

# %%

# Definimos el número de registros para nuestro dataset interactivo
n_rows = 100

# Generamos un rango de fechas consecutivas para el análisis temporal
dates = pd.date_range(start="2026-01-01", periods=n_rows, freq="D")

# Generamos categorías aleatorias (ej. tipos de productos/servicios)
categories = np.random.choice(
    ["Categoría A", "Categoría B", "Categoría C"], size=n_rows
)

# Generamos valores continuos para variables numéricas (Ventas, Satisfacción y Costo)
sales = (
    np.random.normal(loc=200, scale=50, size=n_rows)
    + np.sin(np.linspace(0, 10, n_rows)) * 30
)
satisfaction = np.random.uniform(low=1, high=10, size=n_rows)
costs = sales * 0.6 + np.random.normal(loc=0, scale=10, size=n_rows)

# Lista de palabras para simular datos de texto (comentarios de clientes)
sample_words = [
    "excelente",
    "servicio",
    "bueno",
    "rápido",
    "calidad",
    "producto",
    "atención",
    "malo",
    "lento",
    "recomiendo",
]
text_data = " ".join(np.random.choice(sample_words, size=300))

# Consolidamos todo en un DataFrame de Pandas
df = pd.DataFrame(
    {
        "fecha": dates,
        "categoria": categories,
        "ventas": sales,
        "satisfaccion": satisfaction,
        "costos": costs,
    }
)


# %%

# ==========================================
# 1. UNIVARIATE ANALYSIS
# ==========================================

# # Quick histogram of numerical columns
plt.figure(figsize=(10, 6))
df.hist()
plt.tight_layout()
plt.show()

# %%
# # Box plot showing distribution
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y="ventas")
plt.title("Boxplot de Ventas")
plt.show()

# %%
# # Density plot for continuous variables
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df["ventas"])
plt.title("Densidad de Ventas")
plt.show()

# %%
# # Bar plot for categorical data
plt.figure(figsize=(10, 6))
df["categoria"].value_counts().plot(kind="bar")
plt.title("Conteo por Categoría")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# %%
# ==========================================
# 2. BIVARIATE ANALYSIS
# ==========================================

# %%
# # Relationship between two variables
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="ventas", y="costos")
plt.title("Relación Ventas vs Costos")
plt.show()

# %%
# # Scatter with regression line
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x="ventas", y="costos")
plt.title("Regresión Ventas vs Costos")
plt.show()

# %%
# # Compare categories with bars
plt.figure(figsize=(10, 6))
sns.barplot(x="categoria", y="ventas", data=df)
plt.title("Ventas Promedio por Categoría")
plt.show()

# %%
# # Distribution by category
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x="categoria", y="ventas")
plt.title("Distribución de Ventas por Categoría")
plt.show()

# %%
# # Compare distributions between categories
plt.figure(figsize=(10, 6))
sns.boxplot(x="categoria", y="ventas", data=df)
plt.title("Comparación de Boxplots por Categoría")
plt.show()

# %%
# ==========================================
# 3. MULTIVARIATE ANALYSIS
# ==========================================


# %%
# # Matrix of scatter plots
sns.pairplot(df[["ventas", "satisfaccion", "costos"]])
plt.show()

# %%
# # Correlation matrix heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df[["ventas", "satisfaccion", "costos"]].corr(), annot=True)
plt.title("Matriz de Correlación")
plt.show()

# %%
# # Combined distribution and scatter
sns.jointplot(data=df, x="ventas", y="costos")
plt.show()

# %%
# # Scatter with color-coded third variable
plt.figure(figsize=(10, 6))
plt.scatter(df["ventas"], df["costos"], c=df["satisfaccion"])
plt.xlabel("Ventas")
plt.ylabel("Costos")
plt.title("Ventas vs Costos (Color = Satisfacción)")
plt.colorbar(label="Satisfacción")
plt.show()

# %%
# # Scatter with categorical third variable
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="ventas", y="costos", hue="categoria")
plt.title("Ventas vs Costos por Categoría")
plt.show()

# %%
# ==========================================
# 4. TIME SERIES ANALYSIS
# ==========================================

# %%
# # Basic time series plot
plt.figure(figsize=(10, 6))
df.plot(x="fecha", y="ventas")
plt.title("Serie Temporal de Ventas")
plt.show()

# %%
# # Moving average plot
plt.figure(figsize=(10, 6))
df["ventas"].rolling(window=7).mean().plot()
plt.title("Media Móvil de Ventas (7 días)")
plt.show()

# %%
# # Decompose series into components
df_ts = df.set_index("fecha")
decomposition = seasonal_decompose(df_ts["ventas"], model="additive", period=7)
decomposition.plot()
plt.show()

# %%
# # Time series with confidence intervals
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="fecha", y="ventas")
plt.title("Serie Temporal de Ventas con Intervalo de Confianza")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
# ==========================================
# 5. TEXT DATA ANALYSIS
# ==========================================

# %%
# # Generate word cloud from text
plt.figure(figsize=(10, 6))
wc = WordCloud(width=800, height=400, background_color="white").generate(text_data)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de Palabras")
plt.show()

# %%
# # Word frequency distribution
words = text_data.split()
fdist = FreqDist(words)
plt.figure(figsize=(10, 6))
fdist.plot(10, title="Frecuencia de Palabras")
plt.show()

# %%
# # Bar plot of word frequencies
words_freq = pd.DataFrame(fdist.most_common(10), columns=["words", "frequencies"])
plt.figure(figsize=(10, 6))
sns.barplot(x="words", y="frequencies", data=words_freq)
plt.title("Top 10 Palabras Más Frecuentes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
# ==========================================
# 6. CUSTOMIZATION & 7. SAVING & DISPLAYING
# ==========================================

# # Set figure size for plots
plt.figure(figsize=(10, 6))

# %%
# Dibujamos un gráfico de ejemplo para aplicar las personalizaciones
sns.scatterplot(data=df, x="ventas", y="satisfaccion")

# %%
# # Add title to plot
plt.title("Personalización Completa de Gráfico")

# %%
# # Add x-axis label
plt.xlabel("Ventas Realizadas ($)")

# %%
# # Add y-axis label
plt.ylabel("Puntaje de Satisfacción (1-10)")

# %%
# # Rotate x-axis labels
plt.xticks(rotation=45)

# %%
# # Adjust subplot parameters
plt.tight_layout()

# %%
# # Save plot to file
plt.savefig("grafico_personalizado.png")

# %%
# # Display the plot
plt.show()

# %%
# # Close current plot
plt.close()

# %%
