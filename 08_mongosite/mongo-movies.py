#Team Liusers: Claire Liu and Alex Liu
#SoftDev2 pd6
#K #07: Import/Export Bank
#2019-03-04

'''
https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json

American movies scraped from Wikipedia (contains: year, genre, name, cast, director)

mongoimport --db Liusers --collection movies --drop --jsonArray --file DIRECTORY_NAME/movies.json
'''

import pymongo
import json
server_address="134.209.67.113"
connection=pymongo.MongoClient(server_address)
db=connection.Liusers
collection=db.movies

'''
filename = "movies.json"
movielist = open(filename, "r")
movies = json.load(movielist)
collection.insert_many(movies)
'''

def title_movie(title):
    return collection.find({'title':title})

def genre_movie(genre):
    return collection.find({'genres':genre})

def year_movie(year):
    return collection.find({'year':year})

def lessthan_year(year):
    return collection.find({'year':{'$lt':year}})

def year_and_genre(year,genre):
    return collection.find({'year': year, 'genre': genre})

def display(collection):
    for i in collection:
        print(i['title'])
        #print(i)

#Testing
print('--------------------------------TESTING YEAR---------------------')
display(year_movie(2015))
print('--------------------------------TESTING GENRE---------------------')
display(genre_movie("Comedy"))

