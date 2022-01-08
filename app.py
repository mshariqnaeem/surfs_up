from flask import Flask

# create flask application instance named "app"
app = Flask(__name__)

#Create flask routes
@app.route('/')
def hello_world():
    return 'Hello world'
    