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
    for i in range(2011,2021):
        try:
            i = pd.read_csv(eda_project_path + sep + 'data' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) + '-utf8.csv')
        except:
            try:
                i = pd.read_csv(eda_project_path + sep + 'data' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'-utf8.csv', sep=';')
            except:
                i = pd.read_excel(eda_project_path + sep + 'data' + sep + folder + sep + str(i) + sep + str(i) + porcion_fichero + str(i) +'.xlsx')
        lista_df.append(i)
    return lista_df



def columna_vs_columna(lista_dataframes, posicion_df1, posicion_df2):
    ''' Compara los nombres de las columnas de 2 dataframes que se encuentran en una lista, tomando como argumento la posición de dicho dataframe en la lista.
    
    Tener en cuenta que, para aplicarla, ambos dataframes deben tener la misma cantidad de columnas. '''
    try:
        for pos, valor in enumerate(lista_dataframes[posicion_df1].columns == lista_dataframes[posicion_df2].columns):
            if valor == False:
                print('         Posición de columna diferente: ' + str(pos))
                print('         ---------------------------------')
                print('         Columna de DF en posición ' + str(posicion_df1) + ': ' + lista_dataframes[posicion_df1].columns[pos])
                print('         Columna de DF en posición ' + str(posicion_df2) + ': ' + lista_dataframes[posicion_df2].columns[pos])
                print('         ================================================\n')
    except:
        print('Los dataframes a comparar deben tener la misma cantidad de columnas.')



def comparar_columnas(lista_dataframes): 
    ''' SE DEBE INGRESAR UNA LISTA DE DATAFRAMES A COMPARAR. '''
    for i in range(len(lista_dataframes)):
            for j in range(1, len(lista_dataframes)):    
                if i < j:
                    if len(lista_dataframes[i].columns) == len(lista_dataframes[j].columns):
                        columnas_iguales = lista_dataframes[i].columns == lista_dataframes[j].columns # TRUE si coinciden, FALSE si no
                        if all(columnas_iguales):
                            print('Las columnas de ' + str(i) + ' (' + str(len(lista_dataframes[i].columns)) +') y ' + str(j)+ ' (' + str(len(lista_dataframes[j].columns)) + ') COINCIDEN.')
                            print('======================================================')
                            break
                        else:
                            print('\nLas columnas de ' + str(i) + ' (' + str(len(lista_dataframes[i].columns)) +') y ' + str(j) + ' (' + str(len(lista_dataframes[j].columns)) + ') SON DISTINTAS.\n')
                            columna_vs_columna(lista_dataframes, i, j)
                    else:
                        print(str(i) +  ' (' + str(len(lista_dataframes[i].columns))  + ') y ' + str(j) + ' (' + str(len(lista_dataframes[j].columns)) + ') tienen distinta CANTIDAD de columnas.')
                        print('======================================================')



def mostrar_columnas(lista_dataframes):
    ''' SE DEBE INGRESAR UNA LISTA DE DATAFRAMES '''
    for i in range(len(lista_dataframes)):
        print('Columnas de dataframe en posición ' + str(i) + ':')
        print('------------------------------------')
        print(lista_dataframes[i].columns)
        print('\nNúmero de columnas: ' + str(len(lista_dataframes[i].columns)) + '\n')
        print('===========================================================================================')



def nombre_cada_columna(lista_dataframes):
    tamanio_columnas = []
    for df in lista_dataframes:
        tamanio_columnas.append(len(df.columns))
        a = max(tamanio_columnas)
    for i in range(0,a):
        print('Columna en posición ' + str(i) + '\n')
        for j in range(len(lista_dataframes)):
            try:
                print('DF en posición ' + str (j) + ': ' + str(lista_dataframes[j].columns[i]))
            except:
                print('DF en posición ' + str (j) + ': No contiene columnas en la posición ' + str(i))
        print('\n-------------------------------------\n')



def ver_ultimas_columnas(lista_dataframes):
    tamanio_columnas = []
    for df in lista_dataframes:
        tamanio_columnas.append(len(df.columns))
        a = max(tamanio_columnas)
    for i in range(len(lista_dataframes)):
        if len(lista_dataframes[i].columns) == (a-2):
            print('Posición del DF ' + str(i) + ': '+ str(list(lista_dataframes[i].columns[-2::])))
        elif len(lista_dataframes[i].columns) == a:
            print('Posición del DF ' + str(i) + ': ' + str(list(lista_dataframes[i].columns[-4::])))



def eliminar_columnas_finales(lista_dataframes):
    tamanio_columnas = []
    for df in lista_dataframes:
        tamanio_columnas.append(len(df.columns))
        a = max(tamanio_columnas)
    for i in range(len(lista_dataframes)):
        if len(lista_dataframes[i].columns) == a:
            lista_dataframes[i] = lista_dataframes[i].iloc[:,:(a-2)]



def ordenar_columnas_finales(lista_dataframes):
    tamanio_columnas = []
    for df in lista_dataframes:
        tamanio_columnas.append(len(df.columns))
        a = max(tamanio_columnas)
    for i in range(len(lista_dataframes)):
        if (lista_dataframes[i].columns[-1] == 'Coordenada UTM (X)') or (lista_dataframes[i].columns[-1] == 'Coordenada_UTM_X'):
            col = lista_dataframes[i].columns.to_list()
            col2 = col[0:(a-2)] + col[-1:] + col[-2:-1]
            lista_dataframes[i] = lista_dataframes[i][col2]



def renombrar_columnas(lista_dataframes, lista_nombres):
    for i in range(len(lista_dataframes)):
        lista_dataframes[i].columns = lista_nombres



def unificar_lista_dataframe(lista_dataframes):
    df_concatenados = pd.DataFrame()
    for i in range(1, len(lista_dataframes)):
        df_concatenados = df_concatenados.append(lista_dataframes[i], ignore_index = True)
    return df_concatenados



def crear_listas_personas():
    ''' Crea una lista de los valores de los datasets de personas que son de interés para el dataset en cuestión. '''
    global lista_numero_expediente
    global lista_persona
    global lista_edad
    global lista_sexo
    lista_numero_expediente = []
    lista_persona = []
    lista_edad = []
    lista_sexo = []
    for i in range(len(lista_df_personas)):
        for pos, value in enumerate(lista_df_personas[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_personas[i].iloc[:,pos])
            if 'persona' in value.lower():
                lista_persona.extend(lista_df_personas[i].iloc[:,pos])
            if 'edat' in value.lower():
                lista_edad.extend(lista_df_personas[i].iloc[:,pos])
            if 'sexe' in value.lower():
                lista_sexo.extend(lista_df_personas[i].iloc[:,pos])
    return lista_numero_expediente, lista_persona, lista_edad, lista_sexo