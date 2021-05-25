def enlistar_dataframes_gu():
    global lista_df_gu
    lista_df_gu = []
    for i in range(11,21):
        try:
            i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_GU_BCN_20'+str(i)+'-utf8.csv')
        except:
            try:
                i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_GU_BCN_20'+str(i)+'-utf8.csv', sep=';')
            except:
                i = pd.read_excel('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_GU_BCN_20'+str(i)+'.xlsx')
        lista_df_gu.append(i)
    return lista_df_gu

def enlistar_dataframes_causa():
    global lista_df_causa
    lista_df_causa = []
    for i in range(11,21):
        try:
            i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_CAUSES_GU_BCN_20'+str(i)+'-utf8.csv')
        except:
            try:
                i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_CAUSES_GU_BCN_20'+str(i)+'-utf8.csv', sep=';')
            except:
                i = pd.read_excel('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_CAUSES_GU_BCN_20'+str(i)+'.xlsx')
        lista_df_causa.append(i)
    return lista_df_causa

def enlistar_dataframes_persona():
    global lista_df_persona
    lista_df_persona = []
    for i in range(11,21):
        try:
            i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_PERSONES_GU_BCN_20'+str(i)+'-utf8.csv')
        except:
            try:
                i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_PERSONES_GU_BCN_20'+str(i)+'-utf8.csv', sep=';')
            except:
                i = pd.read_excel('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_PERSONES_GU_BCN_20'+str(i)+'.xlsx')
        lista_df_persona.append(i)
    return lista_df_persona

def enlistar_dataframes_tipo():
    global lista_df_tipo
    lista_df_tipo = []
    for i in range(11,21):
        try:
            i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_TIPUS_GU_BCN_20'+str(i)+'-utf8.csv')
        except:
            try:
                i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_TIPUS_GU_BCN_20'+str(i)+'-utf8.csv', sep=';')
            except:
                i = pd.read_excel('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_TIPUS_GU_BCN_20'+str(i)+'.xlsx')
        lista_df_tipo.append(i)
    return lista_df_tipo

def enlistar_dataframes_vehiculo():
    global lista_df_vehiculo
    lista_df_vehiculo = []
    for i in range(11,21):
        try:
            i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_VEHICLES_GU_BCN_20'+str(i)+'-utf8.csv')
        except:
            try:
                i = pd.read_csv('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_VEHICLES_GU_BCN_20'+str(i)+'-utf8.csv', sep=';')
            except:
                i = pd.read_excel('20'+str(i)+'/20'+str(i)+'_ACCIDENTS_VEHICLES_GU_BCN_20'+str(i)+'.xlsx')
        lista_df_vehiculo.append(i)
    return lista_df_vehiculo

def comparar_columnas(lista_df): 
    ''' SE DEBE INGRESAR UNA LISTA DE DATAFRAMES A COMPARAR. '''
    for i in range(len(lista_df)):
            for j in range(1, len(lista_df)):    
                if i < j:
                    #print(str(i) + ' vs. ' + str(j))
                    if len(lista_df[i].columns) == len(lista_df[j].columns):
                        #print('--------')
                        columnas_iguales = lista_df[i].columns == lista_df[j].columns # TRUE si coinciden, FALSE si no
                        if all(columnas_iguales):
                            print('Las columnas de ' + str(i) + ' (' + str(len(lista_df[i].columns)) +') y ' + str(j)+ ' (' + str(len(lista_df[j].columns)) + ') COINCIDEN.')
                            print('======================================================')
                            break
                        else:
                            print('Las columnas de ' + str(i) + ' (' + str(len(lista_df[i].columns)) +') y ' + str(j) + ' (' + str(len(lista_df[j].columns)) + ') SON DISTINTAS.')
                            print('======================================================')
                    else:
                        print(str(i) +  ' (' + str(len(lista_df[i].columns))  + ') y ' + str(j) + ' (' + str(len(lista_df[j].columns)) + ') tienen distinta CANTIDAD de columnas.')
                        print('======================================================')
                        # print(lista_dataframes[i].columns) == lista_dataframes[j].columns)
                        #print('-------')

def mostrar_columnas(lista_df):
    ''' SE DEBE INGRESAR UNA LISTA DE DATAFRAMES '''
    for i in range(len(lista_df)):
        print('Columnas de dataframe en posición ' + str(i) + ':')
        print('------------------------------------')
        print(lista_df[i].columns)
        print('\nNúmero de columnas: ' + str(len(lista_df[i].columns)) + '\n')
        print('===========================================================================================')
