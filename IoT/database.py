import pyrebase
import os

config = {
  "apiKey": "",
  "authDomain": "",
  "databaseURL": "https://smart-dustbin-e369d.firebaseio.com/",
  "storageBucket":""
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

db.child("All Bins").child("Bin 1").update({"Bio_percent": 25})
