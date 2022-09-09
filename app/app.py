import threading
from flask import Flask, render_template, url_for, redirect
from pymongo import MongoClient
import time

app = Flask(__name__)

# conexion = MongoDB(app)
client = MongoClient('localhost')
database = client['currencyapp']


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
    countdown(countDownTime)


countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()


def getDocuments(currency='dava'):
    collection = database[currency]
    return collection.find({})


@app.route('/<currency>')
def index(currency='dava'):
    global currencyName

    if currency == 'dava':
        currencyName = 'Endava'

    if currency == 'ec':
        currencyName = 'Ecopetrol'

    if currency == 'ibm':
        currencyName = 'IBM'

    if currency == 'btc':
        currencyName = 'Bitcoin'

    if currency == 'eth':
        currencyName = 'Ethereum'

    if currency == 'ada':
        currencyName = 'Cardano'

    data = {
        'currency': "💱 " + currencyName,
        'abbreviation': currency.upper(),
        'documents': getDocuments(currency),
    }

    return render_template('index.html', data=data, countdown=my_timer)

def pageNotFound(error):
    return redirect(url_for('index/dava'))


if __name__ == '__main__':
    app.register_error_handler(404, pageNotFound)
    app.run(debug=True, port=5000)
