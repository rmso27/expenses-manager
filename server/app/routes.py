## IMPORTS ##

# Import modules
from flask import request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from app import app
import configparser

# Import functions from "functions.py" file
from .functions import test_db_conn

## MAIN VARS ##

# CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup configuration file
config = configparser.ConfigParser()
config.read('configs/configs.ini')

# DB info
db_host = config['database']['DB_HOST']
db = config['database']['DB']
db_user = config['database']['DB_USER']
db_password = config['database']['DB_PASSWORD']
db_conn_timeout = config['database']['DB_CONN_TIMEOUT']

## ROUTES ##

# Status route
@app.route('/status')
@cross_origin()
def test_srv_conn():

    '''
        Returns a dictionary with BE server and DB connectivity statuses
    '''

    db_status = test_db_conn(db_host, db, db_user, db_password, db_conn_timeout)
    response = {
        'server': 'OK',
        'database': db_status
    }

    return response