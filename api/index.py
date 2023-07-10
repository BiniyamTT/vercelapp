from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, BiniyamT!'

@app.route('/about')
def about():
    return 'About'