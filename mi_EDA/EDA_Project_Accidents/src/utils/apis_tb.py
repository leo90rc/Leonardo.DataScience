# Contains the generic functionality related to working with APIs.

import json
import pandas as pd
import os
import sys


dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

def csv_to_json(path_fichero):
    dataframe_accidentes = pd.read_csv(eda_project_path + sep + 'data' + sep + 'DATA_POST_CLEANING' + sep + 'accidentes.csv')
    json_accidentes = dataframe_accidentes.to_json(indent = 4)
    return json_accidentes
