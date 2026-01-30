import sqlalchemy
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def query_records():
    return jsonify({'car': 
                    { 'id' : 1,
                     'brand' : 'BMW',  
                    'model' : '316i'},
                    })