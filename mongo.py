#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 14:21:07 2018

@author: mshokry
"""

from flask import Flask,render_template, request, jsonify
from flask_pymongo import PyMongo
from pusher import Pusher
import json

app = Flask(__name__)

# connect to another MongoDB server altogether
# mongo ds163870.mlab.com:63870/hrsys -u <dbuser> -p <dbpassword> 
app.config['MONGO3_HOST'] = 'ds163870.mlab.com'
app.config['MONGO3_PORT'] = 63870
app.config['MONGO3_DBNAME'] = 'hrsys'
app.config['MONGO3_USERNAME'] = 'mshokry'
app.config['MONGO3_PASSWORD'] = '#$m7moud(M)'
mongo = PyMongo(app, config_prefix='MONGO3')

@app.route('/')
def home_page():
    online_users = mongo.db.users.find({'online': True})
    print(online_users)
    return ("Some One Onlie")

@app.route('/user/<username>')
def user_profile(username):
    user = mongo.db.users.find_one_or_404({'_id': username})
    print(user)
    #users = Flask.json_decoder(user)
    return ("USer Exists")

