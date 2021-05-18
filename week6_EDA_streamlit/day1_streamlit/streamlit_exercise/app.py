# -*- coding: utf-8 -*-
import streamlit as st
import os
from utils.stream_config import draw_map
from utils.dataframes import load_normal_csv, load_csv_for_map


path = os.path.dirname(__file__)
menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenida", "Analizador", "Mapa con Globos"])

if menu == 'Bienvenida':
    st.title('¡Bienvenidos al Bootcamp de The Bridge')
    st.write('Es un placer tenerte por aquí')

if menu == "Analizador":
    slider_csv = st.sidebar.file_uploader("Selecciona un CSV", type=['csv'])
    # Cargar el dataframe
    if type(slider_csv) != type(None):  # Se cumple cuando subamos un archivo
        filtro_edades = st.sidebar.checkbox("Filtrar edades")
        df_slider = load_normal_csv(slider_csv)
        if filtro_edades:
            df_slider = df_slider[df_slider["age"] < 10]
        st.bar_chart(df_slider)  # Mostrar gráfico de todo el DF
        st.table(df_slider)  # Muestra el dataframe

if menu == "Mapa con Globos":
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

