from src import app, db
import re
import datetime
from src.models import User, UserSchema
from flask import jsonify, request, abort
from flask_restful import Resource
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

class Register(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', email):
            abort(400, message='email is not valid.')
        if len(password) < 6:
            abort(400, message='password is too short.')
        if db.users.find({'email': email}).count() != 0:
            if db.users.find_one({'email': email})['active'] == True:
                abort(400, message='email is alread used.')
        else:
            db.users.insert_one(
                {'email': email, 'password': generate_password_hash(password), 'active': False})
        exp = datetime.datetime.utcnow(
        ) + datetime.timedelta(days=app.config['ACTIVATION_EXPIRE_DAYS'])
        encoded = jwt.encode({'email': email, 'exp': exp},
                             app.config['KEY'], algorithm='HS256')
        message = 'Hello\nactivation_code={}'.format(encoded.decode('utf-8'))
        msg = Message(recipients=[email],
                      body=message,
                      subject='Activation Code')
        mail.send(msg)
        return {'email': email}


class Activate(Resource):
    def put(self):
        activation_code = request.json['activation_code']
        try:
            decoded = jwt.decode(
                activation_code, app.config['KEY'], algorithms='HS256')
        except jwt.DecodeError:
            abort(400, message='Activation code is not valid.')
        except jwt.ExpiredSignatureError:
            abort(400, message='Activation code is expired.')
        email = decoded['email']
        db.users.update({'email': email}, {'$set': {'active': True}})
        return {'email': email}


class Login(Resource):
    def get(self):
      json_data = request.get_json(force=True)
      if not json_data:
          return {'message': 'No input data provided'}, 400
      email = request.json['email']
      password = request.json['password']
      if User.query.filter_by(email= email).count() == 0:
          return {'message': 'User is not found.'}, 400
      user = User.query.filter_by(email= email).first()
      if not check_password_hash(user.passworhash, password):
          return {'message': 'Password is incorrect.'}, 400
      exp = datetime.datetime.utcnow(
      ) + datetime.timedelta(hours=app.config['TOKEN_EXPIRE_HOURS'])
      encoded = jwt.encode({'email': email, 'exp': exp},
                            app.config['KEY'], algorithm='HS256')
      return {'email': email, 'token': encoded.decode('utf-8')}
