import streamlit as st
import pandas as pd 
import requests

# API URL
url = "https://api-colombia.com/api/v1/President"

# Get response
response = requests.get(url)

# Check status code
if response.status_code == 200:

    # Get data
    data = response.json()
    
    # Create list of dicts from data 
    presidents = [{
        "name": d["name"],
        "lastName": d["lastName"],
        "startPeriodDate": d["startPeriodDate"],
        "endPeriodDate": d["endPeriodDate"],  
    } for d in data]
    
    # Create DataFrame 
    df = pd.DataFrame(presidents)
    
    # Filtrar por nombre
    filter_name = st.text_input("Filtrar por nombre")
    if filter_name:
        df = df[df["name"].str.contains(filter_name, case=False)]
    
    # Filtrar por periodo
    filter_period = st.text_input("Filtrar por periodo")
    if filter_period:
        df = df[df["startPeriodDate"].str.contains(filter_period, case=False) |
                df["endPeriodDate"].str.contains(filter_period, case=False)]
    
    # Mostrar el DataFrame filtrado
    st.write(df)    
    
else:
    st.error("Ocurrió un error")
