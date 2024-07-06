import streamlit as st
import pandas as pd

# Creamos un DataFrame de ejemplo con información de vehículos
vehiculos_data = {
    'Modelo': ['Ford', 'Toyota', 'Honda', 'Chevrolet', 'Nissan', 'Kia'],
    'Ventas 2020': [100000, 90000, 80000, 70000, 60000, 50000],
    'Ventas 2021': [120000, 95000, 85000, 75000, 65000, 55000]
}
vehiculos_df = pd.DataFrame(vehiculos_data)

# Establecemos la columna 'Modelo' como índice del DataFrame
vehiculos_df.set_index('Modelo', inplace=True)

# Creamos un gráfico de línea con las ventas de los vehículos por año
st.line_chart(vehiculos_df[['Ventas 2020', 'Ventas 2021']])
