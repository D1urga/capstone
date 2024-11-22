from pymongo import MongoClient

# Replace with your MongoDB URI
client = MongoClient("mongodb+srv://anoop:anoop1234@cluster0.y9iyb.mongodb.net/databases?retryWrites=true&w=majority&appName=Cluster0")

# Connect to a specific database
db = client['databases']

# Example: Accessing a collection
collection = db['data']

result = collection.find({})
print(result[1])