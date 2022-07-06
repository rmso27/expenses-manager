## IMPORTS ##

# Import modules
from flask import request, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from app import app
import configparser

## MAIN VARS ##

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup configuration file
config = configparser.ConfigParser()
config.read('configs/configs.ini')

## ROUTES ##

# Test route
@app.route('/test')
@cross_origin()
def test():

    response = {'response': 200}

    return response