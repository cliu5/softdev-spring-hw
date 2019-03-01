import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.test

data=db['primer-dataset']


def borough(b):
    return data.find({"borough":b})

def zipcode(z):
    return data.find({"address.zipcode":(z)})

def zipgrade(z,g):
    return data.find({"$and":[{"address.zipcode":z},{"grades.grade": g}]})

def score(s):
    return data.find({"grades.score":{'$lt':s}})


