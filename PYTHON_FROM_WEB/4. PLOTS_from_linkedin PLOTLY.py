# %%
# Importamos las librerías necesarias para el análisis, generación de datos y visualización interactiva
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud
import nltk
from nltk.probability import FreqDist
from statsmodels.tsa.seasonal import seasonal_decompose

# Configuración de semilla para reproducibilidad de los datos
np.random.seed(42)

# %%
# ==========================================
# CREACIÓN DEL DATASET ÚNICO
# ==========================================

n_rows = 100
dates = pd.date_range(start="2026-01-01", periods=n_rows, freq="D")
categories = np.random.choice(
    ["Categoría A", "Categoría B", "Categoría C"], size=n_rows
)

sales = (
    np.random.normal(loc=200, scale=50, size=n_rows)
    + np.sin(np.linspace(0, 10, n_rows)) * 30
)
satisfaction = np.random.uniform(low=1, high=10, size=n_rows)
costs = sales * 0.6 + np.random.normal(loc=0, scale=10, size=n_rows)

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

# # Quick histogram of numerical columns (Subplots interactivos)
fig = make_subplots(rows=1, cols=3, subplot_titles=["ventas", "satisfaccion", "costos"])
fig.add_trace(go.Histogram(x=df["ventas"], name="ventas"), row=1, col=1)
fig.add_trace(go.Histogram(x=df["satisfaccion"], name="satisfaccion"), row=1, col=2)
fig.add_trace(go.Histogram(x=df["costos"], name="costos"), row=1, col=3)
fig.update_layout(height=400, title_text="Histogramas de Variables Numéricas")
fig.show()

# %%
# # Box plot showing distribution
fig = px.box(df, y="ventas", title="Boxplot de Ventas")
fig.show()

# %%
# # Density plot for continuous variables (Histograma con curva de densidad/violín)
fig = px.violin(
    df, y="ventas", box=True, points="all", title="Distribución y Densidad de Ventas"
)
fig.show()

# %%
# # Bar plot for categorical data
cat_counts = df["categoria"].value_counts().reset_index()
cat_counts.columns = ["categoria", "conteo"]
fig = px.bar(cat_counts, x="categoria", y="conteo", title="Conteo por Categoría")
fig.show()

# %%
# ==========================================
# 2. BIVARIATE ANALYSIS
# ==========================================

# %%
# # Relationship between two variables
fig = px.scatter(df, x="ventas", y="costos", title="Relación Ventas vs Costos")
fig.show()

# %%
# # Scatter with regression line
fig = px.scatter(
    df, x="ventas", y="costos", trendline="ols", title="Regresión Ventas vs Costos"
)
fig.show()

# %%
# # Compare categories with bars
fig = px.bar(
    df, x="categoria", y="ventas", barmode="group", title="Ventas por Categoría"
)
fig.show()

# %%
# # Distribution by category
fig = px.violin(
    df,
    x="categoria",
    y="ventas",
    color="categoria",
    box=True,
    title="Distribución de Ventas por Categoría",
)
fig.show()

# %%
# # Compare distributions between categories
fig = px.box(
    df,
    x="categoria",
    y="ventas",
    color="categoria",
    title="Comparación de Boxplots por Categoría",
)
fig.show()

# %%
# ==========================================
# 3. MULTIVARIATE ANALYSIS
# ==========================================

# %%
# # Matrix of scatter plots
fig = px.scatter_matrix(
    df,
    dimensions=["ventas", "satisfaccion", "costos"],
    color="categoria",
    title="Matriz de Dispersión",
)
fig.show()

# %%
# # Correlation matrix heatmap
corr = df[["ventas", "satisfaccion", "costos"]].corr()
fig = px.imshow(corr, text_auto=True, title="Matriz de Correlación")
fig.show()

# %%
# # Combined distribution and scatter (Marginal plots)
fig = px.scatter(
    df,
    x="ventas",
    y="costos",
    marginal_x="histogram",
    marginal_y="box",  # Corregido: 'box' en lugar de 'boxplot'
    title="Distribución Combinada Ventas vs Costos",
)
fig.show()

# %%
# # Scatter with color-coded third variable
fig = px.scatter(
    df,
    x="ventas",
    y="costos",
    color="satisfaccion",
    title="Ventas vs Costos (Color = Satisfacción)",
)
fig.show()

# %%
# # Scatter with categorical third variable
fig = px.scatter(
    df,
    x="ventas",
    y="costos",
    color="categoria",
    title="Ventas vs Costos por Categoría",
)
fig.show()

# %%
# ==========================================
# 4. TIME SERIES ANALYSIS
# ==========================================

# %%
# # Basic time series plot
fig = px.line(df, x="fecha", y="ventas", title="Serie Temporal de Ventas")
fig.show()

# %%
# # Moving average plot
df["ventas_ma7"] = df["ventas"].rolling(window=7).mean()
fig = px.line(
    df, x="fecha", y=["ventas", "ventas_ma7"], title="Ventas y Media Móvil (7 días)"
)
fig.show()

# %%
# # Decompose series into components
df_ts = df.set_index("fecha")
decomp = seasonal_decompose(df_ts["ventas"], model="additive", period=7)
fig = make_subplots(
    rows=4, cols=1, subplot_titles=["Observed", "Trend", "Seasonal", "Residual"]
)
fig.add_trace(
    go.Scatter(x=df["fecha"], y=decomp.observed, name="Observed"), row=1, col=1
)
fig.add_trace(go.Scatter(x=df["fecha"], y=decomp.trend, name="Trend"), row=2, col=1)
fig.add_trace(
    go.Scatter(x=df["fecha"], y=decomp.seasonal, name="Seasonal"), row=3, col=1
)
fig.add_trace(go.Scatter(x=df["fecha"], y=decomp.resid, name="Residual"), row=4, col=1)
fig.update_layout(height=800, title_text="Descomposición de Serie Temporal")
fig.show()

# %%
# # Time series with confidence intervals (Simulado mediante rangos)
fig = px.line(df, x="fecha", y="ventas", title="Serie Temporal con Rangos")
fig.add_traces(
    [
        go.Scatter(
            x=df["fecha"],
            y=df["ventas"] + 15,
            mode="lines",
            line=dict(width=0),
            showlegend=False,
        ),
        go.Scatter(
            x=df["fecha"],
            y=df["ventas"] - 15,
            mode="lines",
            line=dict(width=0),
            fill="tonexty",
            fillcolor="rgba(0,100,80,0.2)",
            name="Intervalo",
        ),
    ]
)
fig.show()

# %%
# ==========================================
# 5. TEXT DATA ANALYSIS
# ==========================================

# %%
# # Generate word cloud from text (Renderizado como imagen en Plotly)
wc = WordCloud(width=800, height=400, background_color="white").generate(text_data)
fig = px.imshow(wc, title="Nube de Palabras")
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
fig.show()

# %%
# # Word frequency distribution
words = text_data.split()
fdist = FreqDist(words)
words_freq = pd.DataFrame(fdist.most_common(10), columns=["words", "frequencies"])
fig = px.line(
    words_freq, x="words", y="frequencies", markers=True, title="Frecuencia de Palabras"
)
fig.show()

# %%
# # Bar plot of word frequencies
fig = px.bar(
    words_freq,
    x="words",
    y="frequencies",
    color="frequencies",
    title="Top 10 Palabras Más Frecuentes",
)
fig.show()

# %%
# ==========================================
# 6. CUSTOMIZATION & 7. SAVING & DISPLAYING
# ==========================================

# %%
# Configuración y personalización avanzada
fig = px.scatter(
    df, x="ventas", y="satisfaccion", color="categoria", hover_data=["costos"]
)

# # Add title & labels
fig.update_layout(
    title="Personalización Completa en Plotly",
    xaxis_title="Ventas Realizadas ($)",
    yaxis_title="Puntaje de Satisfacción (1-10)",
    template="plotly_dark",  # Tema oscuro interactivo
    width=900,
    height=500,
)

# # Rotate x-axis labels
fig.update_xaxes(tickangle=45)

# # Save plot to interactive HTML file
fig.write_html("grafico_personalizado.html")

# # Display the plot
fig.show()
