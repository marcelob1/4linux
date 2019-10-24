#!/usr/bin/python3

import pymongo

try:
    client = pymongo.MongoClient('127.0.0.1')
    db = client['dexterops']

except Exception as e:
    print(e)