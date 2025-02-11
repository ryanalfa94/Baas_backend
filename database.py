from pymongo import MongoClient

# connect to mongodb locally
client = MongoClient("mongodb://localhost:27017")

# Create or connect to a database named 'baas_db '
db = client.baas_db 

# Create a users collection
users_collection = db.users