from flask import Flask, render_template, request, redirect
from database import DatabaseHandler
from routes.home import homeBP
from routes.userManagement import signupBP, createUserBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'
db = DatabaseHandler('appData.db')


##routing
app.register_blueprint(homeBP)
app.register_blueprint(signupBP)
app.register_blueprint(createUserBP)


  
#########
app.run(debug = True)