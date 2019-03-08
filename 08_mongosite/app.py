# Claire Liu
# SoftDev1 pd06
# K#00 
# yyyy-mm-dd

from flask import Flask, render_template, request,session, url_for, redirect, flash
import pymongo
import json
import os

server_address="134.209.67.113"
connection=pymongo.MongoClient(server_address)
db=connection.CCUP
collection=db.movies

@app.route("/")
@app.route("/home",methods=["POST"])
def mongodb():
    if request.form.get('ipaddress')!= None:
        try:
            connection=pymongo.MongoClient(request.form.get("ipaddress"))
            connection.server_info()
            db=connection.CCUP
            collection=db.movies
        except:
            server_address="134.209.67.113"
            connection=pymongo.MongoClient(server_address)
            db=connection.CCUP
            collection=db.movies
    

if __name__ == "__main__":
    app.debug = True
    app.run()

