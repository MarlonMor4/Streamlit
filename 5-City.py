import streamlit as st
import pandas as pd 
import requests

url = "https://api-colombia.com/api/v1/City"

# Get response
response = requests.get(url)

# Check status code
if response.status_code == 200:

    # Get data
    data = response.json()
    
    # Create list of dicts from data 
    cities = [{
        "name": d["name"],
        "department": d["department"],
        "population": d["population"],
        "area": d.get("area", None),  
    } for d in data]
    
    # Create DataFrame 
    df = pd.DataFrame(cities)
    
    # Filtrar por nombre de departamento
    filter_name = st.text_input("Filtrar por nombre")
    if filter_name:
        if filter_name.lower() in df["name"].str.lower().values:
            df = df[df["name"].str.lower() == filter_name.lower()]
        else:
            st.warning("El nombre del departamento no coincide. Ingrese un nombre válido.")
    
    # Filtrar por población mínima
    filter_population = st.slider("Filtrar por población mínima", min_value=0, max_value=int(df["population"].max()), step=1000)
    df = df[df["population"] >= filter_population]
    
    # Mostrar el DataFrame filtrado
    st.write(df)    
    
else:
    st.error("Ocurrió un error")



