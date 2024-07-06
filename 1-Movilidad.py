import streamlit as st
import pandas as pd



# Define el título de la aplicación
st.title("Movilidad Incidentes 2022 - Medellín")

# Carga el archivo csv con los datos
data = pd.read_csv('movilidad_incidentes_2022.csv')
df = pd.DataFrame(data)

# Renombra las columnas para una mejor legibilidad
df = df.rename(columns={'LATITUD': 'LAT'})
df = df.rename(columns={'LONGITUD': 'LON'})
df = df.rename(columns={'CLASE': 'TIPO_INCIDENTE'})

# Selecciona el mes y el día de los incidentes a visualizar
month = st.selectbox('MES', df["MES"].sort_values(ascending=True).unique())
day = st.selectbox('DÍA', df["DIA"].sort_values(ascending=True).unique())

# Selecciona el tipo de incidente y la comuna de los incidentes a visualizar
tipos_incidentes = df["TIPO_INCIDENTE"].sort_values(ascending=True).unique()
tipo_incidente_seleccionado = st.selectbox('TIPO DE INCIDENTE', tipos_incidentes)
comunas = df["COMUNA"].sort_values(ascending=True).unique()
comuna_seleccionada = st.selectbox('COMUNA', comunas)

# Convierte la columna "FECHA" en tipo datetime y filtra los incidentes por mes, día, tipo de incidente y comuna
df['FECHA'] = pd.to_datetime(df['FECHA'])
filtro = (df['MES'] == month) & (df['DIA'] == day) & (df['TIPO_INCIDENTE'] == tipo_incidente_seleccionado) & (df['COMUNA'] == comuna_seleccionada)

# Crea un nuevo dataframe con los incidentes filtrados, selecciona las columnas de latitud y longitud
df_filtrado = df.loc[filtro] 
df_filtrado = df_filtrado.loc[:, ['LAT', 'LON']]    

# Crea un mapa con los incidentes filtrados
st.map(df_filtrado)
