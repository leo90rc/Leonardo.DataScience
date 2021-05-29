#  Contains the generic functionality related to collect data, clean data and others (wrangling methods such us working with multiples jsons).

import pandas as pd
import sys
import os


def datos_por_numero_expediente(lista_dataframes, posicion_dataframe, numero_expediente, nombre_columna_expediente):
    ''' posición_dataframe (int)
        numero_expediente (str)
        nombre_columna_expediente (str) '''
    return lista_dataframes[posicion_dataframe][lista_dataframes[posicion_dataframe][nombre_columna_expediente] == numero_expediente].unstack()



def info_df_enlistado(lista_dataframes):
    for i in range(len(lista_dataframes)):
        print('Información de dataframe en posición '+ str(i))
        print('---------------------------------------')
        print(lista_dataframes[i].info())
        print('______________________________________________________________________________________________________________________________\n')



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



def crear_df_personas(lista_df_personas):
    ''' Crea un dataframe de los valores de los datasets de "personas implicadas en accidentes" que son de interés para el caso en cuestión. '''
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
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_persona, lista_edad, lista_sexo)), columns= ['NUMERO EXPEDIENTE', 'TIPO PERSONA', 'EDAD', 'SEXO'])



def crear_df_causas(lista_df_causas):
    ''' Crea un dataframe de los valores de los datasets de "causas de accidente" que son de interés para el caso en cuestión. '''
    lista_numero_expediente = []
    lista_causas = []
    for i in range(len(lista_df_causas)):
        for pos, value in enumerate(lista_df_causas[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_causas[i].iloc[:,pos])
            if 'causa' in value.lower():
                lista_causas.extend(lista_df_causas[i].iloc[:,pos])
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_causas)), columns= ['NUMERO EXPEDIENTE', 'DESCRIPCION CAUSA'])



def crear_df_tipos(lista_df_tipos):
    ''' Crea un dataframe de los valores de los datasets de "tipos de accidente" que son de interés para el caso en cuestión. '''
    lista_numero_expediente = []
    lista_tipo_accidente = []
    for i in range(len(lista_df_tipos)):
        for pos, value in enumerate(lista_df_tipos[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_tipos[i].iloc[:,pos])
            if 'accident' in value.lower():
                lista_tipo_accidente.extend(lista_df_tipos[i].iloc[:,pos])
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_tipo_accidente)), columns= ['NUMERO EXPEDIENTE', 'TIPO ACCIDENTE'])



def crear_df_vehiculos(lista_df_vehiculos):
    ''' Crea un dataframe de los valores de los datasets de "vehículos implicados en accidentes" que son de interés para el caso en cuestión. '''
    lista_numero_expediente = []
    lista_tipo_vehiculo = []
    lista_modelo = []
    lista_marca = []
    lista_color = []
    lista_tipo_carnet = []
    lista_antiguedad = []
    lista_causa_peaton = []
    for i in range(len(lista_df_vehiculos)):
        for pos, value in enumerate(lista_df_vehiculos[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_vehiculos[i].iloc[:,pos])
            if ('tipus' in value.lower()) and ('vehicle' in value.lower()):
                lista_tipo_vehiculo.extend(lista_df_vehiculos[i].iloc[:,pos])
            if 'model' in value.lower():
                lista_modelo.extend(lista_df_vehiculos[i].iloc[:,pos])
            if 'marca' in value.lower():
                lista_marca.extend(lista_df_vehiculos[i].iloc[:,pos])
            if 'color' in value.lower():
                lista_color.extend(lista_df_vehiculos[i].iloc[:,pos])
            if ('descripció carnet' in value.lower()) or ('descripcio_carnet' in value.lower()):
                lista_tipo_carnet.extend(lista_df_vehiculos[i].iloc[:,pos])
            if 'antiguitat' in value.lower():
                lista_antiguedad.extend(lista_df_vehiculos[i].iloc[:,pos])
            if 'vianant' in value.lower():
                lista_causa_peaton.extend(lista_df_vehiculos[i].iloc[:,pos])
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_tipo_vehiculo, lista_modelo, lista_marca, lista_color, lista_tipo_carnet, lista_antiguedad, lista_causa_peaton)), columns= ['NUMERO EXPEDIENTE', 'TIPO VEHICULO', 'MODELO VEHICULO', 'MARCA VEHICULO', 'COLOR VEHICULO', 'TIPO CARNET', 'ANTIGUEDAD CARNET', 'CAUSA PEATON'])



def crear_df_gu(lista_df_gu):
    ''' Crea un dataframe de los datos recopilados que son de interés para el estudio en cuestión. '''
    lista_numero_expediente = []
    lista_distrito = []
    lista_barrio = []
    lista_calle = []
    lista_dia_semana = []
    lista_ano = []
    lista_mes = []
    lista_dia = []
    lista_hora = []
    lista_turno = []
    lista_victimas = []
    lista_leves = []
    lista_graves = []
    lista_muertos = []
    for i in range(len(lista_df_gu)):
        for pos, value in enumerate(lista_df_gu[i].columns):
            if 'expedient' in value.lower():
                lista_numero_expediente.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('districte' in value.lower()):
                lista_distrito.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('barri' in value.lower()):
                lista_barrio.extend(lista_df_gu[i].iloc[:,pos])
            if ('nom' in value.lower()) and ('carrer' in value.lower()):
                lista_calle.extend(lista_df_gu[i].iloc[:,pos])
            if (('descripció' in value.lower()) or ('descripcio' in value.lower())) and ('setmana' in value.lower()):
                lista_dia_semana.extend(lista_df_gu[i].iloc[:,pos])
            if ('any' in value.lower()) and ('mes' not in value.lower()):
                lista_ano.extend(lista_df_gu[i].iloc[:,pos])
            if ('mes' in value.lower()) and ('nom' in value.lower()):
                lista_mes.extend(lista_df_gu[i].iloc[:,pos])
            if ('mes' in value.lower()) and ('dia' in value.lower()):
                lista_dia.extend(lista_df_gu[i].iloc[:,pos])
            if ('hora' in value.lower()) and ('dia' in value.lower()):
                lista_hora.extend(lista_df_gu[i].iloc[:,pos])
            if 'torn' in value.lower():
                lista_turno.extend(lista_df_gu[i].iloc[:,pos])
            if ('víctimes' in value.lower()) or ('victimes' in value.lower()):
                lista_victimas.extend(lista_df_gu[i].iloc[:,pos])
            if 'lleus' in value.lower():
                lista_leves.extend(lista_df_gu[i].iloc[:,pos])
            if 'greus' in value.lower():
                lista_graves.extend(lista_df_gu[i].iloc[:,pos])
            if 'morts' in value.lower():
                lista_muertos.extend(lista_df_gu[i].iloc[:,pos])
    return pd.DataFrame(list(zip(lista_numero_expediente, lista_distrito, lista_barrio, lista_calle, lista_dia_semana,
    lista_ano, lista_mes, lista_dia, lista_hora, lista_turno, lista_victimas, lista_leves, lista_graves, lista_muertos)),
    columns= ['NUMERO_EXPEDIENTE', 'DISTRITO', 'BARRIO', 'CALLE', 'DIA_SEMANA', 'ANO', 'MES', 'DIA', 'HORA', 'TURNO', 'NUMERO_VICTIMAS',
    'VICTIMAS_LEVES', 'VICTIMAS_GRAVES', 'VICTIMAS_FALLECIDAS'])




#if __name__ == '__main__':



def quitar_espacios(df):
    for columna in df.columns:
        try:
            df[columna] = df[columna].str.strip()
        except:
            pass



def translate(df):
    lista_castellano = ['Mañana', 'Tarde', 'Noche', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    lista_catalan = ['Matí', 'Tarda', 'Nit', 'Gener', 'Febrer', 'Març', 'Abril', 'Maig', 'Juny', 'Juliol', 'Agost', 'Setembre', 'Octubre', 'Novembre', 'Desembre', 'Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge']
    df.replace(lista_catalan, lista_castellano, inplace = True)