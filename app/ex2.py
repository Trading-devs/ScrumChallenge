import pymongo
import json 
import requests
import pandas as pd



from flask import Flask
from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import time




app = Flask(__name__)
app.config['MONGO_URI']= 'mongodb://localhost/ex2db'
mongo= PyMongo(app)


@app.route('/')
def index():
    return 'Web App with Python Flask!'

# @app.route('/users', methods =['POST'])
# def add():
#     Endava=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/DAVA?apikey=2c18aef9c283317435d76672c51df35d')
#     Endava=Endava.json()
#     id = mongo.db.ada.insert_many(Endava)
    
#     Ecopetrol=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/EC?apikey=2c18aef9c283317435d76672c51df35d')
#     Ecopetrol=Ecopetrol.json()
#     id = mongo.db.ec.insert_many(Ecopetrol)
    
#     IBM=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/IBM?apikey=2c18aef9c283317435d76672c51df35d')
#     IBM=IBM.json()
#     id = mongo.db.ibm.insert_many(IBM)
    
@app.route('/dava',methods=['GET'])
def get_dava():
    
    Endava=requests.get('https://financialmodelingprep.com/api/v3/quote-short/DAVA?apikey=2c18aef9c283317435d76672c51df35d')
    Endava=Endava.json()
    
    mongo.db.dava.insert_many(Endava)
    
    users = mongo.db.dava.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )
    
@app.route('/ec',methods=['GET'])
def get_ec():
    Ecopetrol=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/EC?apikey=2c18aef9c283317435d76672c51df35d')
    Ecopetrol=Ecopetrol.json()
    mongo.db.ec.insert_many(Ecopetrol)
    
    users = mongo.db.ec.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )

@app.route('/ibm',methods=['GET'])
def get_ibm():
    IBM=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/IBM?apikey=2c18aef9c283317435d76672c51df35d')
    IBM=IBM.json()
    mongo.db.ibm.insert_many(IBM)
    
    users = mongo.db.ibm.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )



@app.route('/btc',methods=['GET'])
def get_btc():
    btc=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/BTC-USD?apikey=2c18aef9c283317435d76672c51df35d')
    btc=btc.json()
    mongo.db.btc.insert_many(btc)
    
    users = mongo.db.btc.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )

@app.route('/eth',methods=['GET'])
def get_eth():
    eth=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/ETH-USD?apikey=2c18aef9c283317435d76672c51df35d')
    eth=eth.json()
    mongo.db.eth.insert_many(eth)
    
    users = mongo.db.eth.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )

@app.route('/ada',methods=['GET'])
def get_ada():
    ada=requests.get('https://financialmodelingprep.com/api/v3/historical-chart/5min/ADA-USD?apikey=2c18aef9c283317435d76672c51df35d')
    ada=ada.json()
    mongo.db.ada.insert_many(ada)
    
    users = mongo.db.ada.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=81) #localhost -> 81

# i=1 
# while i ==1:
   


    
#     time.sleep(300)
