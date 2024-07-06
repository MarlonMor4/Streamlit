import streamlit as st
import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('diabetes.csv')

# Mostrar el DataFrame
st.write(data)

# Obtener las opciones únicas de género
gender_options = data['gender'].unique()

# Crear una lista desplegable para seleccionar el género
selected_gender = st.selectbox('Seleccionar género', gender_options)

# Obtener la columna de interés para el gráfico de barras
column_options = ['age', 'hypertension', 'heart_disease', 'smoking_history', 'bmi', 'HbA1c_level', 'blood_glucose_level', 'diabetes']
selected_column = st.selectbox('Seleccionar columna', column_options)

# Filtrar el DataFrame en función del género seleccionado
filtered_df = data[data['gender'] == selected_gender]

# Graficar el DataFrame filtrado con un gráfico de barras
st.bar_chart(filtered_df[selected_column].value_counts())

