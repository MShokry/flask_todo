from flask_restful import Resource
from src.models import Todo, TodoSchema
from src import db
from flask import request

todos_schema = TodoSchema(many=True)
todo_schema = TodoSchema(strict=True)

class Task(Resource):
  def get(self):
    todos = Todo.query.all()
    todos = todos_schema.dump(todos).data
    return {'status': 'success', 'data': todos}, 200
  
  def post(self):
    json_data = request.get_json(force=True)
    if not json_data:
            return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = todos_schema.load(json_data)
    if errors:
        return errors, 422
    todos = Todo.query.filter_by(name=data['task']).first()
    if todos:
        return {'message': 'todos already exists'}, 400
    todos = Todo(
        task=json_data['task']
        )
    db.session.add(todos)
    db.session.commit()
    result = todos_schema.dump(todos).data
    return { "status": 'success', 'data': result }, 201
  
  def put(self):
    json_data = request.get_json(force=True)
    if not json_data:
            return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = todo_schema.load(json_data)
    if errors:
        return errors, 422
    todo = todo.query.filter_by(id=data['id']).first()
    if not todo:
        return {'message': 'todo does not exist'}, 400
    todo.name = data['name']
    db.session.commit()

    result = todo_schema.dump(todo).data

    return { "status": 'success', 'data': result }, 204
  
  def delete(self):
    json_data = request.get_json(force=True)
    if not json_data:
            return {'message': 'No input data provided'}, 400
    # Validate and deserialize input
    data, errors = todo_schema.load(json_data)
    if errors:
        return errors, 422
    todo = Todo.query.filter_by(id=data['id']).delete()
    db.session.commit()

    result = todo_schema.dump(todo).data

    return { "status": 'success', 'data': result}, 204
