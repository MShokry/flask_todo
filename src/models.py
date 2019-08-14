from src import db, ma 

from datetime import datetime
from marshmallow import Schema, fields, pre_load, validate


class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(300), index=True, unique=True, nullable=False)
  email = db.Column(db.String(200), index=True, unique=True)
  passworhash= db.Column(db.String(128))
  posts = db.relationship('Todo', backref='author', lazy='dynamic')

  def __repr__(self):
    return '<USER {}>'.format(self.username)

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'email')
  

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, task,done,user_id):
      self.task = task
      self.doen = done
      self.user_id = user_id

    def __repr__(self):
      return '<Task %r >' % self.id

class TodoSchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  task = fields.String(required=True)
  done = fields.Integer(required=False, validate=validate.Length(1))
  date_created = fields.DateTime()
  class Meat:
    fields = ('id', 'task', 'done', 'date_created')
