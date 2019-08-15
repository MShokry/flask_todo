from src import app,db
from src.models import User, UserSchema
from flask import jsonify, request
from flask_restful import Resource
from flask_httpauth import HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash


user_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True)

class Users(Resource):
  def get(self):
    all_users = User.query.all()
    result = users_schema.dump(all_users).data
    return {'status': 'success', 'data': result}, 200 

  def post(self):
    json_data = request.get_json(force=True)
    if not json_data:
            return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = user_schema.load(json_data)
    if errors:
        return errors, 422
    users = User.query.filter_by(email=data['email']).first()
    if users:
        return {'message': 'users already exists'}, 400
    users = User(
        username=json_data['username'],
        email=json_data['email'],
        passworhash=json_data['passworhash'],
    )
    db.session.add(users)
    db.session.commit()
    result = user_schema.dump(users).data
    return {"status": 'success', 'data': result}, 201

  def delete(self):
    json_data = request.get_json(force=True)
    if not json_data:
            return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = user_schema.load(json_data)
    if errors:
        return errors, 422
    user = User.query.filter_by(id=data['id']).delete()
    db.session.commit()
    result = user_schema.dump(user).data
    return {"status": 'success', 'data': result}, 204

  # Get Single users
  @app.route('/user/<id>', methods=['GET'])
  def get_user(self, id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

  # Update a user
  @app.route('/user/<id>', methods=['PUT'])
  def update_user(id):
    user = User.query.get_or_404(id)

    username = request.json['username']
    email = request.json['email']
    passworhash = request.json['password']

    user.username = username
    user.email = email
    user.passworhash = passworhash

    db.session.commit()

    return user_schema.jsonify(user)

  
