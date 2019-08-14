from flask import Flask, Blueprint
from flask_restful import Api

from src import app

if __name__ == "__main__":
    app.run(debug=True)