import pandas as pd
import numpy as np
import json

def open_file(path_file):
    """
    Read a json file

    Args:
        path_file ([str]): Path where is the file
    """
    # TODO (@gabvaztor) This function must open a file and write something.
    with open(path_file, 'r+') as outfile:
        json_data_indented_readed = json.load(outfile)
    return json_data_indented_readed

def delete_file():
    # TODO (@gabvaztor)
    pass 