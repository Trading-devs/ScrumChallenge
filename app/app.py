import threading
from flask import Flask, render_template, url_for, redirect, jsonify, Response, request
from pymongo import MongoClient
from flask_pymongo import PyMongo
import json
import requests
import time
import pandas as pd
from bson import json_util
from bson.objectid import ObjectId
from datetime import datetime, date
from re import T

# email.mime subclasses
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Para iniciar flask o la aplicacion como tal dar - > python app/app.py

app = Flask(__name__)


# Email configuration
def send_email(ticker,price,date,percentage):
    # Define the HTML document
    html =  '''
<html>
    
 <head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

/* Style the body */
body {{
  font-family: Arial;
  margin: 0;
}}

/* Header/Logo Title */
.header {{
  padding: 10px;
  text-align: center;
  background: #000000;
  color: white;
  font-size: 30px;
}}

/* Page Content */
.content {{
	padding:20px;
	color: #000000;
	text-align: center;
}}

body {{
  background-image: url('https://cdn.pixabay.com/photo/2017/08/10/01/42/stock-market-2616931_960_720.jpg');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position: center;
}}

footer {{
  text-align: center;
  padding: 3px;
  background-color: #000000;
  color: white;
}}

</style>
</head>



<body>

<div class="header">
  <h1>Stock Alert!</h1>
</div>

<div class="content">
  <h1>Ticker.</h1>
  <h2>{}</h2>
  <h1>Price:</h1>
  <h2>{}</h2>
  <h1>Date and hour:</h1>
  <h2>{}</h2>
  <h1>Comparisson with previous prices:</h1>
  <h2>{}%</h2>

</div>

</body>

<footer>
	<p>Author: Trading Devs</p>
	<p><a href="tradingdevs@example.com">tradingdevs@example.com</a></p>
</footer>

  
</html>
'''
    html=html.format(ticker,price,date,percentage)

    # Set up the email addresses and password. Please replace below with your email address and password
    email_from = 'jp232277@gmail.com'
    password = 'udtxiejvfapmsqpz'
    email_to = 'jp232277@gmail.com'

    # Generate today's date to be included in the email Subject
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

    # Create a MIMEMultipart class, and set up the From, To, Subject fields
    email_message = MIMEMultipart()
    email_message['From'] = email_from
    email_message['To'] = email_to
    email_message['Subject'] = f'Alert Stock!! - {date_str}'

    # Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()

    # Connect to the Gmail SMTP server and Send Email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)


# Conection = MongoDB(app)
client = MongoClient('localhost')
database = client['challengedb']


# A collection for each database
dava = database["dava"]
ec = database["ec"]
ibm = database["ibm"]
ada = database["ada"]
btc = database["btc"]
eth = database["eth"]


# Hour
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# Date
today = date.today()

# Complete date and hour
current_date = (str(today) + ' / ' + str(current_time))


# Insert data in mongoDB
def insert_dava():
    print('Enadava')
    Endava = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/DAVA?apikey=130539b6c85bda9f602da3c028aff9ba')
    Endava = Endava.json()
    Endava[0]['date'] = current_date
    dava.insert_many(Endava)


def insert_ec():
    print('Ecopetrol')
    Ecopetrol = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/EC?apikey=130539b6c85bda9f602da3c028aff9ba')
    Ecopetrol = Ecopetrol.json()
    Ecopetrol[0]['date'] = current_date
    ec.insert_many(Ecopetrol)


def insert_ibm():
    print('IBM')
    IBM = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/IBM?apikey=130539b6c85bda9f602da3c028aff9ba')
    IBM = IBM.json()
    IBM[0]['date'] = current_date
    ibm.insert_many(IBM)


def insert_btc():
    print('Bitcoin')
    BTC = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/BTC-USD?apikey=130539b6c85bda9f602da3c028aff9ba')
    BTC = BTC.json()
    BTC[0]['date'] = current_date
    btc.insert_many(BTC)


def insert_eth():
    print('Ethereum')
    ETH = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/ETH-USD?apikey=130539b6c85bda9f602da3c028aff9ba')
    ETH = ETH.json()
    ETH[0]['date'] = current_date
    eth.insert_many(ETH)


def insert_ada():
    print('Cardano')
    ADA = requests.get(
        'https://financialmodelingprep.com/api/v3/quote-short/ADA-USD?apikey=130539b6c85bda9f602da3c028aff9ba')
    ADA = ADA.json()
    ADA[0]['date'] = current_date
    ada.insert_many(ADA)

 # Get dataframe  from each collection


def get_dava():
    records = dava.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df


def get_ec():
    records = ec.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df


def get_ibm():
    records = ibm.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df


def get_btc():
    records = btc.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df


def get_eth():
    records = eth.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df


def get_ada():
    records = ada.find()
    records = list(records)
    df = pd.DataFrame(records)
    return df

# Find the average of each collection


def Average(lst):
    return sum(lst) / len(lst)

# Email function


def stock_mail():

    
    dava_df = get_dava()
    current_dava = dava_df['price'].values[-1]
    date_dava = dava_df['date'].values[-1]
    mean_dava = round(Average(dava_df['price'].values[:-1]), 2)
    percent_dava = round(((current_dava-mean_dava)/mean_dava)*100,2)

    if (percent_dava > 20 or percent_dava < -20):
        send_email('DAVA', current_dava,  date_dava , percent_dava)

    ec_df = get_ec()
    current_ec = ec_df['price'].values[-1]
    date_ec = ec_df['date'].values[-1]
    mean_ec = round(Average(ec_df['price'].values[:-1]), 2)
    percent_ec =round(((current_ec-mean_ec)/mean_ec)*100,2)

    if (percent_ec > 20 or percent_ec < -20):
        send_email('EC', current_ec,  date_ec , percent_ec)

    ibm_df = get_ibm()
    current_ibm = ibm_df['price'].values[-1]
    date_ibm = ibm_df['date'].values[-1]
    mean_ibm = round(Average(ibm_df['price'].values[:-1]), 2)
    percent_ibm = round(((current_ibm-mean_ibm)/mean_ibm)*100,2)

    if (percent_ibm > 20 or percent_ibm < -20):
        send_email('IBM', current_ibm,  date_ibm , percent_ibm)

    btc_df = get_btc()
    current_btc = btc_df['price'].values[-1]
    date_btc = btc_df['date'].values[-1]
    mean_btc = round(Average(btc_df['price'].values[:-1]), 2)
    percent_btc = round(((current_btc-mean_btc)/mean_btc)*100,2)

    if (percent_btc > 20 or percent_btc < -20):
        send_email('BTC', current_btc,  date_btc , percent_btc)

    eth_df = get_eth()
    current_eth = eth_df['price'].values[-1]
    date_eth = eth_df['date'].values[-1]
    mean_eth = round(Average(eth_df['price'].values[:-1]), 2)
    percent_eth = round(((current_eth-mean_eth)/mean_eth)*100,2)

    if (percent_eth > 20 or percent_eth < -20):
        send_email('ETH', current_eth,  date_eth , percent_eth)
        
    ada_df = get_ada()
    current_ada = ada_df['price'].values[-1]
    date_ada = ada_df['date'].values[-1]
    mean_ada = round(Average(ada_df['price'].values[:-1]), 2)
    percent_ada = round(((current_ada-mean_ada)/mean_ada)*100,2)

    if (percent_ada > 20 or percent_ada < -20):
        send_email('ADA', current_ada,  date_ada , percent_ada)

    


# Actualizar la base de datos
def updateDatabase():
    print('Updating database...')


# 300 = 5 minutes
def countdown(countDownTime=300):
    global my_timer
    my_timer = countDownTime
    while my_timer > 0:
        time.sleep(1)
        my_timer -= 1
    updateDatabase()
    #insert_dava()
    #insert_ec()
    #insert_ibm()
    #insert_btc()
    #insert_eth()
    #insert_ada()
    stock_mail()
    countdown(countDownTime)


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()


def getDocuments(currency='dava'):
    collection = database[currency]
    return collection.find({})


@app.route('/<currency>', methods=['GET', 'POST'])
def index(currency='dava'):
    global currencyName

    if currency == 'dava':
        currencyName = 'Endava'
        dava_chart=get_dava()
        x=list(dava_chart['date'].values)[-11:]
        y=list(dava_chart['price'].values)[-11:]

    if currency == 'ec':
        currencyName = 'Ecopetrol'
        ec_chart=get_ec()
        x=list(ec_chart['date'].values)[-11:]
        y=list(ec_chart['price'].values)[-11:]

    if currency == 'ibm':
        currencyName = 'IBM'
        ibm_chart=get_ibm()
        x=list(ibm_chart['date'].values)[-11:]
        y=list(ibm_chart['price'].values)[-11:]

    if currency == 'btc':
        currencyName = 'Bitcoin'
        btc_chart=get_btc()
        x=list(btc_chart['date'].values)[-11:]
        y=list(btc_chart['price'].values)[-11:]

    if currency == 'eth':
        currencyName = 'Ethereum'
        eth_chart=get_eth()
        x=list(eth_chart['date'].values)[-11:]
        y=list(eth_chart['price'].values)[-11:]

    if currency == 'ada':
        currencyName = 'Cardano'
        ada_chart=get_ada()
        x=list(ada_chart['date'].values)[-11:]
        y=list(ada_chart['price'].values)[-11:]

    data = {
        'currency': "💱 " + currencyName,
        'abbreviation': currency.upper(),
        'documents': getDocuments(currency),
    }
    


    return render_template('index.html', data=data, countdown=my_timer, labels=x, values=y)


def pageNotFound(error):
    return redirect(url_for('index/dava'))


if __name__ == '__main__':
    app.register_error_handler(404, pageNotFound)
    app.run(debug=False, port=5000)
