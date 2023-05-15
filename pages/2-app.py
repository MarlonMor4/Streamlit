

import streamlit as st
import pandas as pd
import altair as alt

# Cargar la base de datos
data = pd.read_csv('FPL_tweets.csv')

# Filtro por categoría
followers = data['Followers'].unique()
filtro_followers = st.sidebar.selectbox("Seleccione un rango de Followers", followers)
filtered_data = data[data['Followers'] == filtro_followers]

# Filtro por Likes
likes = data['Likes'].unique()
filtro_likes = st.sidebar.selectbox("Seleccione un rango de Likes", likes)
filtered_data = filtered_data[data['Likes'] == filtro_likes]

# Búsqueda por nombre
nombre = st.sidebar.text_input("Buscar por nombre")
filtered_data = filtered_data[data['User'].str.contains(nombre, case=False)]

# Gráfico de barras
chart = alt.Chart(filtered_data).mark_bar().encode(
    x='User',
    y='Likes'
).properties(
    width=alt.Step(30)
)
st.altair_chart(chart, use_container_width=True)

