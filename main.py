from flask import Flask, render_template, request
from database import DatabaseHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'
db = DatabaseHandler('appData.db')


##routing
@app.route("/")
def home():
    return  render_template('index.html')

@app.route("/signup")
def signUp():
    return  render_template('signup.html')

@app.route('/createUser', methods = ['post'])
def createUser():
    username = request.form['username']
    password = request.form['password']
    rePassword = request.form['rePassword']
    if password == rePassword:
        db.createUser(username,password)
        return '<h1> Success </h1>'
    else:
        return '<h1> Passwords Dont match </h1>'

  
#########
app.run(debug = True)