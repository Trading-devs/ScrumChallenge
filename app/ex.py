import threading
from flask import Flask, render_template, url_for, redirect
from flask import Flask, request, jsonify, Response
from pymongo import MongoClient
from flask_pymongo import PyMongo
import json 
import requests
import time
import pandas as pd
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime, date

# Conection = MongoDB(app)
client = MongoClient('localhost')
database = client['challengedb']

#A collection for each database
dava=database["dava"]
ec=database["ec"]
ibm=database["ibm"]
ada=database["ada"]
btc=database["btc"]
eth=database["eth"]

def get_dava():
    records  = dava.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df

def get_ec():
    records  = ec.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df

def get_ibm():
    records = ibm.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df

def get_btc():
    records  = btc.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df

def get_eth():
    records  = eth.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df

def get_ada():
    records  = ada.find()
    records =list(records)
    df=pd.DataFrame(records)
    return df


def stock_values():
    dava=get_dava()
    current_dava = dava['price'].values[0]
    mean_dava = round(dava['price'].mean(axis=0),2)
    percent_dava = ((current_dava-mean_dava)/mean_dava)*100
    
    if(percent_dava > 20 or percent_dava < -20):
        print('sentdava')
    
    ec=get_ec()
    current_ec = ec['price'].values[0]
    mean_ec = round(ec['price'].mean(axis=0),2)
    percent_ec = ((current_ec-mean_ec)/mean_ec)*100
    
    if(percent_ec > 20 or percent_ec< -20):
        print('sentec')
    
    ibm=get_ibm()
    current_ibm = ibm['price'].values[0]
    mean_ibm = round(ibm['price'].mean(axis=0),2)
    percent_ibm = ((current_ibm-mean_ibm)/mean_ibm)*100
    
    if(percent_ibm > 20 or percent_ibm < -20):
        print('sentibm')
    
    btc=get_btc()
    current_btc = btc['price'].values[0]
    mean_btc = round(btc['price'].mean(axis=0),2)
    percent_btc = ((current_btc-mean_btc)/mean_btc)*100
    
    if(percent_btc > 20 or percent_btc < -20):
        print('sentbtc')
    
    eth=get_eth()
    current_eth = eth['price'].values[0]
    mean_eth = round(eth['price'].mean(axis=0),2)
    percent_eth = ((current_eth-mean_eth)/mean_eth)*100
    
    if(percent_eth > 20 or percent_eth< -20):
        print('senteth')
    
    ada=get_ada()
    current_ada = ada['price'].values[0]
    mean_ada = round(ada['price'].mean(axis=0),2)
    
    percent_ada = ((current_ada-mean_ada)/mean_ada)*100
    
    if(percent_ada > 20 or percent_ada < -20):
        print('sentada')

def Average(lst):
    return sum(lst) / len(lst)

dava=get_dava()
current_dava = dava['price'].values[-1]
mean_dava =round(Average(dava['price'].values[:-1]),2)
percent_dava = ((current_dava-mean_dava)/mean_dava)*100

x_dava=list(dava['date'].values)
y_dava=list(dava['price'].values)
x_ec=list(ec['date'].values)
y_ec=list(ec['price'].values)
x_ibm=list(ibm['date'].values)
y_ibm=list(ibm['price'].values)
x_btc=list(btc['date'].values)
y_btc=list(btc['price'].values)
x_eth=list(eth['date'].values)
y_eth=list(eth['price'].values)
x_ada=list(ada['date'].values)
y_ada=list(ada['price'].values)

print(x_dava)