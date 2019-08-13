from app import db, ma
from datetime import datetime


class User(db.Model):
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
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
      return '<Task %r >' % self.id
class TodoSchema(ma.Schema):
  class Meat:
    fields = ('id', 'task', 'done', 'date_created')

users_schema = UserSchema(many=True)
user_schema = UserSchema(strict=True)
todos_schema = TodoSchema(many=True,strict=True)
todos_schema = TodoSchema(strict=True)