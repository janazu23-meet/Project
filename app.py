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
app.config['SECRET_KEY'] = "jkbkigyiugyigiy"


@app.route('/members_details')
def members_details():
	return render_template('speaker-details.html')

@app.route('/', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':

		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('index'))
		except: 
		
			error = "Authentication failed"
	return render_template("signin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		user = {"name": request.form['name'], "email": request.form["email"], "password": request.form["password"]}
		db.child("users").child(login_session["user"]["localId"]).set(user)
		try:
			return redirect(url_for('index'))
		except:
			error = "Authentication failed"
		return render_template("signup.html", error=error)
	return render_template("signup.html")

@app.route('/index')
def index():
	username = db.child("users").child(login_session['user']['localId']).get().val()['name']
	return render_template('index.html', username=username)

if __name__ == '__main__':
	app.run(debug=True)