from flask import Flask
from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import yfinance as yf


#Comandos para levantar el entorno virtual -> virtualenv env (nombre del entorno virtual)
# .\env\Scripts\activate.bat
#Para iniciar flask o la aplicacion como tal dar - > python app/challenge.py



app = Flask(__name__)
app.config['MONGO_URI']= 'mongodb://localhost/challengedb'
mongo= PyMongo(app)
    
@app.route('/')
def index():
    data = yf.download(['DAVA','EC','IBM','BTC-USD','ADA-USD','ETH-USD'], period='5m', start='2022-08-24', end='2022-08-31', group_by='ticker')
    df=data.head() # Entrega la fecha , open,adjclose, close, high, low , open, volume

    #return 'Web App with Python Flask!'
    return print( df.to_string())



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81) #localhost -> 81


#-------Poner en le jupyte rnotebook

# import piplite
# await piplite.install(['yfinance'])
# import yfinance as yf

# data = yf.download(['DAVA','EC','IBM','BTC-USD','ADA-USD','ETH-USD'], period='5m', start='2022-08-24', end='2022-08-31', group_by='ticker')
# data.head() # Entrega la fecha , open,adjclose, close, high, low , open, volume