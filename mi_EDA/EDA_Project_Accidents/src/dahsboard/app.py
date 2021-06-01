# Correrá un dashboard streamlit utilizando el comando necesario.

# -*- coding: utf-8 -*-
import os
import sys
dir = os.path.dirname   #LAMETIENFOLDERS_TB
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np




menu = st.sidebar.selectbox('Menu:', options=["Bienvenida", "Accidentes en cada barrio", "API"])



if menu == 'Bienvenida':
    st.title('Accidentes registrados por la Guardia Urbana de Barcelona')
    st.write('En esta web encontrarás todos los accidentes de tráfico que han sido registrados\
            en la ciudad de Barcelona entre los años 2010 y 2020. Además puedes obtener el json\
            del dataframe completo si así lo deseas. ')



if menu == "Accidentes en cada barrio":

    st.title('Accidentes de tráfico en los barrios más turísticos')
    st.write('En la siguiente sección se presentan, evaluados por cada mes, los accidentes de tráfico registados por la Guardia Urbana de la ciudad de Barcelona, para los barrios de mayorr concurrencia de turistas en los meses de temporada alta.')
    menu_barrios = st.selectbox('Barrios:', options=['Seleccione un barrio', 'El Barri Gòtic', 'La Barceloneta', 'El Poble Sec', 'El Poblenou',
'Sant Pere, Santa Caterina i la Ribera', 'La Sagrada Família',
'La Nova Esquerra de l\'Eixample', 'El Fort Pienc', "L'Antiga Esquerra de l'Eixample",
'La Dreta de l\'Eixample', 'Sant Antoni', 'la Vila de Gràcia'])

    if menu_barrios == 'El Barri Gòtic':                                         
        st.write('BARRIO GÓTIC')
        gotic = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'gotic_x_mes.png')
        st.image (gotic,use_column_width=True)
    if menu_barrios == 'La Barceloneta':
        st.write('BARRIO DE LA BARCELONETA')
        barceloneta = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'barceloneta_x_mes.png')
        st.image (barceloneta,use_column_width=True)
    if menu_barrios == 'El Poble Sec':
        st.write('BARRIO DE EL POBLE SEC')
        poble_sec = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'poble_sec_x_mes.png')
        st.image (poble_sec,use_column_width=True)
    if menu_barrios == 'El Poblenou':
        st.write('BARRIO DE EL POBLENOU')
        poblenou = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'poblenou_x_mes.png')
        st.image (poblenou,use_column_width=True)
    if menu_barrios == 'Sant Pere, Santa Caterina i la Ribera':
        st.write('BARRIO SANT PERE, SANTA CATERINA I LA RIBERA')
        ribera = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'ribera_x_mes.png')
        st.image (ribera,use_column_width=True)
    if menu_barrios == 'La Sagrada Família':
        st.write('BARRIO DE LA SAGRADA FAMÍLIA')
        sagrada = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'sagrada_x_mes.png')
        st.image (sagrada,use_column_width=True)
    if menu_barrios == 'La Nova Esquerra de l\'Eixample':
        st.write('BARRIO DE LA NOVA ESQUERRA DE L\'EIXAMPLE')
        nova_esquerra = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'nova_esquerra_x_mes.png')
        st.image (nova_esquerra,use_column_width=True)
    if menu_barrios == 'El Fort Pienc':
        st.write('BARRIO DE EL FORT PIENC')
        fort_pienc = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'fort_pienc_x_mes.png')
        st.image (fort_pienc,use_column_width=True)
    if menu_barrios == "L'Antiga Esquerra de l'Eixample":
        st.write('BARRIO DE L\'ANTIGA ESQUERRA DE L\'ANTIGA ESQUERRA DE L\'EIXAMPLE')
        antigua_esquerra = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'antigua_esquerra_x_mes.png')
        st.image (antigua_esquerra,use_column_width=True)
    if menu_barrios == 'La Dreta de l\'Eixample':
        st.write('BARRIO DE LA DRETA DE L\'EIXAMPLE')
        dreta = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'dreta_x_mes.png')
        st.image (dreta,use_column_width=True)
    if menu_barrios == 'Sant Antoni':
        st.write('BARRIO SANT ANTONI')
        sant_antoni = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'sant_antoni_x_mes.png')
        st.image (sant_antoni,use_column_width=True)
    if menu_barrios == 'la Vila de Gràcia':
            st.write('BARRIO DE LA VILA DE GRACIA')
            vila_gracia = Image.open(eda_project_path + sep + 'reports' + sep + 'plots' + sep + 'vila_gracia_x_mes.png')
            st.image (vila_gracia,use_column_width=True)

if menu == "API":
    st.title('WEB APP')
    st.write('La descarga del CSV comenzará automáticamente.')
    for i in range(2): st.write("")
    st.write('Directorio de destino: EDA_Project_Accidents/data/API_Download')
    st.write('Nombre fichero: accidentes_barcelona_2010-2020.csv')
    dataframe_accidentes = pd.read_json('http://localhost:6060/obtener_json?token_id=Y6571256D')
    st.table(dataframe_accidentes)
    dataframe_accidentes.to_csv(eda_project_path + '/data/API_Download/accidentes_barcelona_2010-2020.csv', index = False, encoding = 'utf-8')