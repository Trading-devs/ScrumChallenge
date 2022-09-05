from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId


#Comandos para levantar el entorno virtual -> virtualenv env (nombre del entorno virtual)
# .\env\Scripts\activate.bat
#Para iniciar flask o la aplicacion como tal dar - > python app/app.py

app=Flask(__name__)
app.config['MONGO_URI']= 'mongodb://localhost/Pruebadb'

mongo= PyMongo(app)

@app.route('/')
def index():
    return 'Web App with Python Flask!'



@app.route('/users', methods =['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    
    if username and email and password:
        id = mongo.db.users.insert_one({'username': username, 'email': email, 'password':password})

        response = {
            'id' : str(id),
            'username': username, 
            'password': password, 
            'email': email         
        } 
        return response
        
    else:
        return not_found()
    return {'message' :'recieved'}




@app.route('/users',methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response=json_util.dumps(users)
    return Response(response , mimetype = 'application/json' )

@app.route('/users/<id>',methods=['GET'])
def get_user(id):
   user = mongo.db.users.find_one({'_id': ObjectId(id)})
   response = json_util.dumps(user)
   return Response(response, mimetype='application/json')

@app.route('/users/<id>',methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id':ObjectId(id)})
    response = jsonify({'message': 'user' + id+ ' was deleted '})
    return response

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify( {
        'message': 'Resource Not Found'+ request.url,
        'status': 404 
    })
    response.status.code=404
    return response
    
        

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
    