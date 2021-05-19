from pymongo import MongoClient
from decouple import config

# Constants 
server = config('MONGODB_SERVER')
port = config('MONGODB_PORT')
database = config('MONGODB_DATABASE')
user = config('MONGODB_USER')
password = config('MONGODB_PASSWORD')

# Create client
client = MongoClient()

# Function
def connectMongoClient():
  global client
  configURI = "mongodb://" + user + ":" + password + "@" + server + ":" + port + "/" + database + "?authSource=admin"
  # configURI = "mongodb://localhost:27017"
  client = MongoClient(configURI)
  print("Connected to mongoDB!! ")

def getCollection(name):
  global client
  print("return collection: ", name)
  return client.cart[name]

def findAll(collection=None, query=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(query is None):
    raise Exception("query is empty")
  return collection.find(query)

def insertOne(collection=None, data=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(data is None):
    raise Exception("data is empty")
  return collection.insert_one(data)

def closeClient():
  global client
  if isinstance(client, MongoClient):
    client.close()