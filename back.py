#!/usr/bin/python3

import cgi
import subprocess
import time
import pymongo

print("content-type:  text/html")
print("Access-Control-Allow-origin: *")
print()

client = pymongo.MongoClient("mongodb+srv://harsh:Ww9nXedEAG5UM8tv@cluster0.yjhpx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.login

f = cgi.FieldStorage()
em = f.getvalue("email")
pa = f.getvalue("pass")
db.info.insert_one({ "email":em, "password":pa})
#o = subprocess.getoutput()
print("Insertion Done")
