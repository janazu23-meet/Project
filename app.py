from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCMmqmZN64L3va-KZuU8G61gj5sDXO-8uE",
  "authDomain": "personal-project-1-5e837.firebaseapp.com",
  "projectId": "personal-project-1-5e837",
  "storageBucket": "personal-project-1-5e837.appspot.com",
  "messagingSenderId": "668340839437",
  "appId": "1:668340839437:web:7d5d143be5076b87f8e144",
  "measurementId": "G-G7966SPQDT",
  "databaseURL": "https://personal-project-1-5e837-default-rtdb.europe-west1.firebasedatabase.app"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)