#  Contains the generic functionality related to open, create, read and write files.

import pandas as pd
import sys
import os


dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)



def enlistar_dataframes(porcion_fichero):
    ''' El argumento debe ser la porción del fichero correspondiente (str). La misma es todo el fragmento del fichero que se encuentra entre los años.
    Ejemplo: Para el fichero "2016_ACCIDENTS_GU_BCN_2016.csv", se debe ingresar "_ACCIDENTS_GU_BCN_"'''
    lista_df = []
    if porcion_fichero == '_ACCIDENTS_GU_BCN_':
        folder = 'ACCIDENTES_GU'
    elif porcion_fichero == '_ACCIDENTS_CAUSES_GU_BCN_':
        folder = 'CAUSAS'
    elif porcion_fichero == '_ACCIDENTS_PERSONES_GU_BCN_':
        folder = 'PERSONA_INVOLUCRADA'
    elif porcion_fichero == '_ACCIDENTS_TIPUS_GU_BCN_':
        folder = 'TIPO'
    elif porcion_fichero == '_accidents_vehicles_gu_bcn_':
        folder = 'VEHICULO'
    for i in range(2010,2021):
        try:
            i = pd.read_csv(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) + '-utf8.csv')
        except:
            try:
                i = pd.read_csv(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'-utf8.csv', sep=';')
            except:
                i = pd.read_excel(eda_project_path + sep + 'data' + sep + 'TO_WRANGLING' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'.xlsx')
        lista_df.append(i)
    return lista_df



def guardar_csv_post_wrangling(lista_df_post_wrangling, lista_nombres_csv):
    ''' Guarda dataframes como CSV en la carpeta DATA_POST_WRANGLING. 
        Args:
            - lista_df_post_wrangling: Lista de dataframes.
            - lista_nombres_csv: Lista de nombres que recibiran los CSV's (tener en cuenta el orden).'''
    for i in zip(lista_df_post_wrangling, lista_nombres_csv):
        i[0].to_csv('../data/DATA_POST_WRANGLING/' + i[1], index = False, encoding = 'utf-8')


def df_to_csv_post_cleaning(df, nombre_archivo):
    ''' Guarda dataframes como CSV en la carpeta DATA_POST_CLEANING. 
        Args:
            - df: El dataframe que se desea guardar.
            - nombre_archivo: Nombre que recibirá el archivo guardado. Debe ser un string finalizado en ".csv".'''
    df.to_csv('../data/DATA_POST_CLEANING/' + nombre_archivo, index = False, encoding = 'utf-8')



dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)

def leer_csv_post_cleaning(nombre_archivo):#nombre_gu = 'df_gu', nombre_causas = 'df_causas', nombre_personas = 'df_personas', nombre_vehiculos = 'df_vehiculos', nombre_tipos = 'df_tipos'):
    ''' Lee un archivo .csv ubicado en la dirección /data/DATA_POST_CLEANING.
        Arg: nombre_archivo: Nombre del archivo que se desea abrir en string (se debe agregar ".csv"). '''
    global df
    df = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_CLEANING' + sep + nombre_archivo)
    return df



dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)

def leer_csv_post_wrangling():#nombre_gu = 'df_gu', nombre_causas = 'df_causas', nombre_personas = 'df_personas', nombre_vehiculos = 'df_vehiculos', nombre_tipos = 'df_tipos'):
    '''El orden de lectura de los ficheros .csv es el siguiente: accidentes_gu.csv, accidentes_causas.csv, accidentes_personas.csv, accidentes_vehiculos.csv, accidentes_tipos.csv.
       Se debe tener en cuenta a la hora de nombrar los dataframes.'''
    global nombre_gu
    global nombre_causas
    global nombre_personas
    global nombre_vehiculos
    global nombre_tipos
    nombre_gu = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_WRANGLING' + sep + 'accidentes_gu.csv')
    nombre_causas = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_WRANGLING' + sep + 'accidentes_causas.csv')
    nombre_personas = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_WRANGLING' + sep + 'accidentes_personas.csv')
    nombre_vehiculos = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_WRANGLING' + sep + 'accidentes_vehiculos.csv')
    nombre_tipos = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_WRANGLING' + sep + 'accidentes_tipos.csv')
    return nombre_gu, nombre_causas, nombre_personas, nombre_vehiculos, nombre_tipos
