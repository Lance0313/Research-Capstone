# firebase_init.py
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("keywords-e2507-firebase-adminsdk-ruto8-cc3abd39a8.json")
firebase_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://keywords-e2507-default-rtdb.firebaseio.com/'
})
print("Firebase initialized successfully.")