from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'THISISABADKEY'





#########
app.run(debug = True)