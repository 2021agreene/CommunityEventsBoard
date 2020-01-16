import os
from app import app
from flask import render_template, request, redirect

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:yEXc16X4d8OuM8b0@cluster0-3ainf.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
    collection = mongo.db.events
    events = list(collection.find({}))
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

# need a get and a post method
@app.route('/results', methods = ["get", "post"])
def results():
    # store userinfo from the form
    user_info = dict(request.form)
    print(user_info)
    #store the event_name
    event_name = user_info["event_name"]
    print("the event name is ",event_name)
    #store the event_date
    event_date = user_info["event_date"]
    print("the event date is ",event_date)
    event_category = user_info["category"]
    print("the event category is ",event_category)
    event_time = user_info["event_time"]
    print("the event time is ",event_time)
    #connect to Mongo DB
    collection = mongo.db.events
    #insert the user's input devent_name and event_date to MONGO
    collection.insert({"event_name": event_name, "event_date": event_date, "event_category": event_category, "event_time": event_time})
    #(so that it will continue to exist after this program stops)
    #redirect back to the index page
    return redirect('/index')

@app.route('/delete_all')
def delete_all():
    collection = mongo.db.events
    collection.delete_many({})
    return redirect('/index')
@app.route('/filter', methods = ["get", "post"])
def function():
    collection = mongo.db.events
    user_input = dict(request.form)
    category = user_input["category"]
    test = list(collection.find({"event_category": category}))
    return render_template('filter.html', events = test)
