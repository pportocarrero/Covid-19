
# Imports
# -----------------------------------------------------------

import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import os
import requests
import csv
from datetime import datetime

# Load data from external source

os.chdir('C:/Users/pport/OneDrive/Projects/Covid-19/')

# DATA CONFIG

data = pd.read_csv('positivos_covid.csv', delimiter = ';')

data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors = 'raise')

nan_values = data['FECHA_RESULTADO'].isna().sum()

data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].fillna('20211231') # NaN values are assigned to 31/12/2021

data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].astype(float, errors = 'raise')

data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'].map('{:.0f}'.format)

data['FECHA_RESULTADO'] = data['FECHA_RESULTADO'] * 1

# WRANGLING

data['YEAR'] = data['FECHA_RESULTADO'].str[2:4]

data['MONTH'] = data['FECHA_RESULTADO'].str[4:6]

data['DAY'] = data['FECHA_RESULTADO'].str[6:8]

data['DATE'] = data['DAY'] + '/' + data['MONTH'] + '/' + data['YEAR']

data['DATE'] = pd.to_datetime(data['DATE'])

data['DATE'] = pd.to_datetime(data['DATE']).dt.strftime('%d/%m/%y')

data["DATE"] = data["DATE"].astype("datetime64")

# REGIONS OF PERU

divisiones = {'Divisiones': ['DEPARTAMENTO', 'PROVINCIA', 'DISTRITO']}

divisiones_df = pd.DataFrame(divisiones)
divisiones_list = divisiones_df['Divisiones'].unique()

regiones = {'Departamento': ['AMAZONAS', 'ANCASH', 'APURIMAC', 'AREQUIPA', 'AYACUCHO', 'CAJAMARCA',
                             'CALLAO', 'CUSCO', 'HUANCAVELICA', 'HUANUCOO', 'ICA', 'JUNIN',
                             'LA LIBERTAD', 'LAMBAYEQUE', 'LIMA', 'LORETO', 'MADRE DE DIOS', 'MOQUEGUA',
                             'PASCO', 'PIURA', 'PUNO', 'SAN MARTIN', 'TACNA', 'TUMBES',
                             'UCAYALI'
                             ]}

reg_df = pd.DataFrame(regiones)
clist = reg_df['Departamento'].unique()

# DATA PROCESSING

reg_select = st.selectbox('Seleccione una división:', divisiones_list)

casos_reg = data[data[divisiones] == clist]

aggregate_region = casos_reg.groupby(['DATE']).size()

df_aggregate_reg = pd.DataFrame({'casos': aggregate_region})
