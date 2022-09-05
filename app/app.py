from flask import Flask, render_template, request, url_for, redirect, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# conexion = MongoDB(app)
client = MongoClient('localhost')
database = client['currencyapp']

def getDocuments(currency='dava'):
    collection = database[currency]
    return collection.find({})

@app.route('/<currency>')
def index(currency='dava'):

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
        'currency': currencyName,
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

def pagina_no_encontrada(error):
    return redirect(url_for('/dava'))

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
