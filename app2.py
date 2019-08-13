from flask import Flask, render_template, request, redirect, jsonify, json
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from flask_marshmallow import Marshmallow

#https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-2-724ebf04d12
# from api import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #db.create_all()
db = SQLAlchemy(app)
ma = Marshmallow(app)

import user

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
      return '<Task %r >' % self.id

class ToDOSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'task', 'done', 'date_created')

todo_schema = ToDOSchema(many=True)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    task_content = request.form['content']
    new_task = ToDo(task=task_content) 
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect('/')
    except:
      return 'There are an issue adding the task'
  
  else:
    tasks = ToDo.query.order_by(ToDo.date_created).all()  
    print(tasks)
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
  task_to_delete = ToDo.query.get_or_404(id)
  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')
  except:
    return 'Unable to delete this task'


@app.route('/update/<int:id>', methods=['GET','POST'])
def edit(id):
  task_to_edit = ToDo.query.get_or_404(id)
  if request.method == 'POST':
    try:
      task = request.form['content']
      task_to_edit.task = task
      db.session.commit()
      return redirect('/')
    except:
      return 'Error updating the task'
  else:
    return render_template('update.html', task=task_to_edit)

@app.route('/tasks', methods=['GET','POST'])
def list_tasks():
    tasks = ToDo.query.order_by(ToDo.date_created).all() 
    result = todo_schema.dump(tasks)
    return jsonify(result.data)

if __name__ == "__main__":
  app.run(debug=True)

