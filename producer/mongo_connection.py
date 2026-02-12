from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['week-17-db']
collection = db['suspicious_customers_orders']
