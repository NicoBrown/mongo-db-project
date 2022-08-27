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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Error")
        
def show_menu():
    print("")
    print("1. Add a record")
    print("2. search a record by name")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter option: ")  
    return option


def main_loop():
    while True:
        option = show_menu()
        if option == "1":  
            print("You have selected option 1")
        elif option == "2": 
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid Option")
        print("")

conn = mongo_connection(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

main_loop()