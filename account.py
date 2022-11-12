### PyMongo to interact with Mongodb ###
from pymongo import MongoClient
import datetime
import time

def mongodb_connexion():
    MONGO_URI = 'mongodb://localhost'
    client = MongoClient(MONGO_URI)

    db = client['test']
    # collection = db['products']
    # products = [{"name": "keyboard", "price": 300}, {"name": "pc", "price": 400}, {"name": "laptop", "price": 700}]
    # collection.insert_many(products)
    return db


def get_users_as_dictionary(file_name):
    separator = ","
    with open(file_name, encoding="utf-8") as file:
        next(file)  # avoid file headers
        users = []
        for line in file:
            line = line.rstrip("\n")  # remove line break
            colums = line.split(separator)
            user_id = colums[0]
            account_type = colums[1]
            account_number = colums[2]
            users.append({
                 "userId": user_id,
                 "accountType": account_type,
                 "accountNumber": account_number,
                 "createdAt": datetime.datetime.now(),
                 "updatedAt": datetime.datetime.now()
                 })

        return users


def save_multiple_user():
    start = time.time()
    db = mongodb_connexion()
    users = get_users_as_dictionary("users_mock.csv")
    collection = db['accounts']
    collection.insert_many(users)
    end = time.time()
    time_seconds = (end - start) * 100
    #print(end - start)
    print(f"Final time to insert 5000 rows {time_seconds}")


save_multiple_user()
