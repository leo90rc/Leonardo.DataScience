# Contains the functionality that starts the Flask API. This file only will be executed if it is passed an argument “-x 8642”, 
# otherwise will show “wrong password”. In the API there is, at least, this GET functions.

# VER EN PDF DE PROYECTO

from flask import Flask, request, render_template
#from utils.apis_tb import read_json
import sys
import os

dir = os.path.dirname
sep = os.sep
api_path = dir(dir(__file__))
sys.path.append(api_path)
print('--')
print(api_path)
print('--')
from utils.apis_tb import read_json


app = Flask(__name__)

@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    return app.send_static_file('greet.html')


@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/info")
def create_json():
    return 'Tienes que acceder al endpoint "/give_me_id" pasando por parámetro "password" con la contraseña correcta' 

# localhost:6060/give_me_id?password=12345
@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['password']
    if x == "12345":
        return request.args
    else:
        return "No es la contraseña correcta"

@app.route("/recibe_informacion")
def recibe_info():
    pass 

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
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