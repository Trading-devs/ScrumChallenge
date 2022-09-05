
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

from datetime import datetime, date


#Hora, minuto y segundo
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Dia
today = date.today()

#Fecha completa
current_date=(str(today) + ':' +str(current_time))

#Insertar fecha
Endava=requests.get('https://financialmodelingprep.com/api/v3/quote-short/DAVA?apikey=2c18aef9c283317435d76672c51df35d')
Endava=Endava.json()
Endava[0]['date'] =current_date





#Insertar fecha
Endava[0]['date'] =current_date

print(Endava)

