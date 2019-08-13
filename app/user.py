from app import app, db
from app.models import User,user_schema,users_schema
from flask import jsonify, request
 

@app.route('/')
@app.route('/index')
def index():
  return 'Hi'

  # Create a user
@app.route('/user', methods=['POST'])
def add_user():
  username = request.json['username']
  email = request.json['email']
  passworhash = request.json['password']
  new_user = User(username=username, email=email, passworhash=passworhash)
  db.session.add(new_user)
  db.session.commit()
  return user_schema.jsonify(new_user)

# Get All users
@app.route('/user', methods=['GET'])
def get_users():
  all_users = User.query.all()
  result = users_schema.dump(all_users)
  return jsonify(result.data)

# Get Single users
@app.route('/user/<id>', methods=['GET'])
def get_user(id):
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

# Delete user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
  user = user.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return user_schema.jsonify(user)
