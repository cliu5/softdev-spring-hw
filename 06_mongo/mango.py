import pymongo
from pymongo import MongoClient

SERVER_ADDR="167.99.158.108"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.restaurants

def get_borough(borough):
    return collection.find( {'borough': borough} )

def get_zipcode(zipcode):
    return collection.find( {'address.zipcode': zipcode} )

def get_zip_grade(zipcode, grade):
    return collection.find( {'address.zipcode': zipcode, 'grades.grade': grade} )

def get_zip_score(zipcode, score):
    return collection.find( {'address.zipcode': zipcode, 'grades.score': {'$lt': score} } )

def display_restaurants(collection):
    for i in collection:
        print(i)


display_restaurants(get_borough("Brooklyn"))
display_restaurants(get_zipcode("11364"))
display_restaurants(get_zip_grade("11364", "B"))
display_restaurants(get_zip_score("11364", 5))
display_restaurants(get_zip_grade_score("11364", "C", 20))
