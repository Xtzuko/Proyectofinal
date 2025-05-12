import streamlit as st
import pandas as pd

# Título de la app
st.title("Explorador de Datos - Proyecto Final Ciencia de datos")

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("/workspaces/movies-dataset/data/train.csv")

df = cargar_datos()

# Mostrar los primeros registros
st.subheader("Vista previa del dataset")
st.dataframe(df.head())

# Mostrar información general
st.subheader("Información general")
st.write(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
st.write("Columnas:")
st.write(df.columns.tolist())

# Estadísticas básicas
st.subheader("Estadísticas descriptivas")
st.write(df.describe())

# Filtro por columna (si hay columnas categóricas o texto)
columnas = df.select_dtypes(include=['object', 'category']).columns
if len(columnas) > 0:
    col = st.selectbox("Selecciona una columna para filtrar", columnas)
    opciones = df[col].unique()
    seleccion = st.selectbox(f"Filtrar por {col}", opciones)
    st.dataframe(df[df[col] == seleccion])

# Gráfico opcional (si hay columnas numéricas)
st.subheader("Gráfico de histograma")
numericas = df.select_dtypes(include=['float64', 'int64']).columns
if len(numericas) > 0:
    col_hist = st.selectbox("Selecciona una columna numérica", numericas)
    st.bar_chart(df[col_hist].value_counts().sort_index())

