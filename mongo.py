import os 
import pymongo

if os.path.exists("env.py"):
    import env
    
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "testDB"
COLLECTION = "celebrities"

def mongo_connection(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is Connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Error")
        
conn = mongo_connection(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

documents = coll.find()
print(documents)
for doc in documents:
    print(doc)