from flask import Blueprint, redirect, render_template, request
from database import DatabaseHandler

db = DatabaseHandler('appData.db')

# Blueprint names
signupBP = Blueprint('signup', __name__)
createUserBP = Blueprint('createUser',__name__)
authUserBp = Blueprint('authUser', __name__)

# Blueprint Routing
@signupBP.route("/signup")
def signUp():
    return  render_template('signup.html')

@createUserBP.route('/createUser', methods = ['post'])
def createUser():
    username = request.form['username']
    password = request.form['password']
    rePassword = request.form['rePassword']
    if password == rePassword:
        responce = db.createUser(username,password)
        if responce == True:
            return redirect('/')
        else:
            return '<h1> Error Making Account </h1>'
            
    else:
        return '<h1> Passwords Dont match </h1>'

@authUserBp.route('/auth', methods = ['post'])
def authUser():
    username = request.form['username']
    password = request.form['password']

    responce = db.authenticate(username ,password)
    if responce == True:
        return '<h1> welcome to the website</h1>'
    else:
        return '<h1> Error loging in</h1>'
