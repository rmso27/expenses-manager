## IMPORTS ##

# Import modules
from flask import request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from app import app
import configparser

# Import functions from "functions.py" file
from .functions import get_db_status

## MAIN VARS ##

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup configuration file
config = configparser.ConfigParser()
config.read('configs/configs.ini')

## ROUTES ##

# Status route
@app.route('/status')
@cross_origin()
def status():

    '''
        Returns a dictionary with BE server and DB connectivity statuses
    '''

    db_status = get_db_status()

    response = {
        'server': 'OK',
        'database': db_status
    }

    print(response)

    return response