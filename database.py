from pymongo import MongoClient
from decouple import config

# Constants 
server = config('MONGODB_SERVER')
port = config('MONGODB_PORT')
database = config('MONGODB_DATABASE')
user = config('MONGODB_USER')
password = config('MONGODB_PASSWORD')
staging_server = config('STAGING_MONGODB_SERVER')
staging_port = config('STAGING_MONGODB_PORT')
staging_database = config('STAGING_MONGODB_DATABASE')
staging_user = config('STAGING_MONGODB_USER')
staging_password = config('STAGING_MONGODB_PASSWORD')

# Create client
client = MongoClient()

# Function
def connectMongoClient():
  global client
  # configURI = "mongodb://" + user + ":" + password + "@" + server + ":" + port + "/" + database + "?authSource=admin"
  # configURI = "mongodb://" + staging_user + ":" + staging_password + "@" + staging_server + ":" + staging_port + "/" + staging_database + "?authSource=admin"
  configURI = "mongodb://localhost:27017"
  client = MongoClient(configURI)
  print("Connected to mongoDB!! ")

def getCollection(name):
  global client
  return client.cart[name]

def findAll(collection=None, query=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(query is None):
    raise Exception("query is empty")
  return collection.find(query)

def findOne(collection=None, query=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(query is None):
    raise Exception("query is empty")
  return collection.find_one(query)

def insertOne(collection=None, data=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(data is None):
    raise Exception("data is empty")
  return collection.insert_one(data)

def updateOne(collection=None,condition=None, data=None):
  if(collection is None):
    raise Exception("collection is empty")
  if(condition is None):
    raise Exception("condition is empty")
  if(data is None):
    raise Exception("data is empty")
  return collection.update_one(condition, data)

def closeClient():
  global client
  if isinstance(client, MongoClient):
    client.close()