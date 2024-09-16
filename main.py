from flask import Flask, render_template




app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'

##routing
@app.route("/")
def home():
    return  render_template('index.html')

@app.route("/signup")
def signUp():
    return  render_template('signup.html')




#########
app.run(debug = True)