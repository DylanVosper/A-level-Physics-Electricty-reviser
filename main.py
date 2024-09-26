from flask import Flask, render_template, request, redirect
from database import DatabaseHandler
from routes.home import homeBP
from routes.userManagement import signupBP, createUserBP, authUserBp, logoutBp
from routes.dashboard import dashboardBp, questionReviserBP, statisticsBP

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'
db = DatabaseHandler('appData.db')


##routing
app.register_blueprint(homeBP)
app.register_blueprint(signupBP)
app.register_blueprint(createUserBP)
app.register_blueprint(authUserBp)
app.register_blueprint(dashboardBp)
app.register_blueprint(logoutBp)
app.register_blueprint(questionReviserBP)
app.register_blueprint(statisticsBP)
  
#########
app.run(debug = True)