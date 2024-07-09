from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, origins="*")

@app.route('/')
def hello():
    return 'Hello'

@app.route('/amit')
def amitkasabe():
    return 'amit kasabe'

# Import your controllers here
from controller import *

if __name__ == '__main__':
    app.run(debug=True)
