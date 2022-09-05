import time
from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# conexion = MongoDB(app)
client = MongoClient('localhost')
database = client['currencyapp']
timer = ''


def updateDatabase():
    # conexion = client['conexion']
    # print(conexion)
    # database.update_one({'_id': conexion._id}, {'$set': {'amount': conexion.amount}})
    print('Updating database...')


def countdown(countdownTime):
    while countdownTime:
        mins, secs = divmod(countdownTime, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        countdownTime -= 1


def getDocuments(currency='dava'):
    collection = database[currency]
    return collection.find({})


@app.route('/<currency>')
def index(currency='dava'):

    currencyName = ''

    if currency == 'dava':
        currencyName = 'Endava'

    elif currency == 'ec':
        currencyName = 'Ecopetrol'

    elif currency == 'ibm':
        currencyName = 'IBM'

    elif currency == 'btc':
        currencyName = 'Bitcoin'

    elif currency == 'eth':
        currencyName = 'Ethereum'

    elif currency == 'ada':
        currencyName = 'Cardano'

    data = {
        'currency': "💱 " + currencyName,
        'abbreviation': currency.upper(),
        'documents': getDocuments(currency),
    }

    return render_template('index.html', data=data)


@app.before_request
def before_request():
    print('Antes de la petición...')


@app.after_request
def after_request(response):
    print('Después de la petición')
    return response


def pageNotFound(error):
    return redirect(url_for('index/dava'))


if __name__ == '__main__':
    app.register_error_handler(404, pageNotFound)
    app.run(debug=True, port=5000)
