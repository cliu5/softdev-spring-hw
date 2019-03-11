#BoatInspired -- Thomas Lee, Claire Liu, Josh Weiner
#SoftDev2 pd6
#K08 -- Ay Mon, Go Git It From Yer Flask
#2019-03-08

from flask import Flask,render_template,request,session
#import mongo
import pymongo
import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)
collection=None
db=None
ip = "157.230.50.34"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get_ip")
def get_ip():
    ip = "157.230.50.34"
    if request.args.get("ip") != None:
        try:
            ip = request.args.get("ip")
            connection = pymongo.MongoClient(ip)
            connection.drop_database("database")
            db = connection["BoatBoatInspire"]
            collection = db["movies"]
            file = open('movies.json')
            data = json.load(file)
            collection.insert_many(data)
        except:
            ip = "157.230.50.34"
            connection = pymongo.MongoClient(ip)
            connection.drop_database("database")
            db = connection["BoatBoatInspire"]
            collection = db["movies"]
            file = open('movies.json')
            data = json.load(file)
            collection.insert_many(data)
    return render_template("search.html",ip=ip)

ip = "157.230.50.34"
connection = pymongo.MongoClient(ip)
connection.drop_database("database")
db = connection["BoatBoatInspire"]
collection = db["movies"]
file = open('movies.json')
data = json.load(file)
collection.insert_many(data)

def title_movie(title):
    movies = collection.find({'title':title})
    return movies

def genre_movie(genre):
    return collection.find({'genres':genre})

def year_movie(year):
    return collection.find({'year':year})

@app.route("/query")
def query():
    results = []
    q = request.args.get("search")
    try:
        date = int(q)
    except:
        date = ""
    new = title_movie(q)
    for movie in new:
        del movie["_id"]
        if movie not in results:
            results.append(movie)
    new = genre_movie(q)
    for movie in new:
        if movie not in results:
            results.append(movie)
    new = year_movie(date)
    for movie in new:
        if movie not in results:
            results.append(movie)
    # print(results)
    return render_template("results.html",results=results)

app.debug = True
app.run()
