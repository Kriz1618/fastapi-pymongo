from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
import os

MONGO_STR = os.environ['MONGO_STRING']

cluster = MongoClient(MONGO_STR, serverSelectionTimeoutMS=5000)
global db

try:
    db = cluster['fastapidb']
    print(' DB conected successfully '.center(50, '*'))
except Exception as err:
    print('Error connecting to the DB server: {}'.format(err))
