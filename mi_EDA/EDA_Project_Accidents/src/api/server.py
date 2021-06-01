# Contains the functionality that starts the Flask API. This file only will be executed if it is passed an argument “-x 8642”, 
# otherwise will show “wrong password”. In the API there is, at least, this GET functions.

import argparse
from flask import Flask, request, render_template
import os
import sys
import json

dir = os.path.dirname
sep = os.sep
eda_project_path = dir(dir(dir(__file__)))
sys.path.append(eda_project_path)


from src.utils.apis_tb import read_json
from src.utils.apis_tb import csv_to_json
# Mandatory
parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int)

args = vars(parser.parse_args())

if args['x'] == 8642:

    app = Flask(__name__)  # name --> main

    # ---------- Flask functions ----------

    # localhost:6060/give_me_id?password=12345
    @app.route('/')
    def ingreso():
        return 'Para obtener el json del dataframe debe acceder al endpoint "/obtener_json" pasando por parámetro la contraseña correcta.\n\
            Inserte en la URL: localhost:6060/obtener_json?token_id="INSERTAR_CONTRASEÑA"'

    @app.route('/obtener_json', methods=['GET'])
    def obtener_json():
        x = request.args['token_id']
        S = "Y6571256D"
        if x == S:
            ubicacion_accidentes = eda_project_path + sep + 'data' + sep + 'DATA_POST_CLEANING' + sep + 'accidentes.csv'
            return csv_to_json(path_fichero = ubicacion_accidentes)
        else:
            return "La contraseña es incorrecta."



    # ---------- Other functions ----------

    def main():
        print("---------STARTING PROCESS---------")
        print(__file__)

        # Get the settings fullpath
        # \ --> WINDOWS
        # / --> UNIX
        # Para ambos: os.sep
        settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
        print(settings_file)
        # Load json from file
        json_readed = read_json(fullpath=settings_file)

        # Load variables from jsons
        SERVER_RUNNING = json_readed["server_running"]
        print("SERVER_RUNNING", SERVER_RUNNING)
        if SERVER_RUNNING:
            DEBUG = json_readed["debug"]
            HOST = json_readed["host"]
            PORT_NUM = json_readed["port"]
            app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
        else:
            print("Server settings.json doesn't allow to start server. " + 
                "Please, allow it to run it.")

    if __name__ == "__main__":
        main()

else:
    print('Wrong password')