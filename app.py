#!flask/bin/python
from flask import Flask, jsonify
from random import randint
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

quotes = [line.rstrip('\n') for line in open('quotes.txt')]

@app.route('/')
def index():
    return 'Hi!'


@app.route('/quotes/api', methods=['GET'])
def get_quote():
    q_id=randint(0,len(quotes)-1);
    return jsonify({'quote':quotes[q_id]})

    
if __name__ == '__main__':
    app.run()
