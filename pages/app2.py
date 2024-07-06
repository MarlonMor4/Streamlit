import streamlit as st # type: ignore
import pandas as pd # type: ignore

def main():
    vehiculos_data = {
        'Modelo': ['Ford', 'Toyota', 'Honda', 'Chevrolet', 'Nissan', 'Kia'],
        'Ventas 2020': [100000, 90000, 80000, 70000, 60000, 50000],
        'Ventas 2021': [120000, 95000, 85000, 75000, 65000, 55000]
    }
    vehiculos_df = pd.DataFrame(vehiculos_data)
    vehiculos_df.set_index('Modelo', inplace=True)
    st.line_chart(vehiculos_df[['Ventas 2020', 'Ventas 2021']])
