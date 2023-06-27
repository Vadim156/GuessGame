from flask import Flask, jsonify, request
import json , time
import random
import requests

random_number = random.randint(1, 100)
numberOfTries = 5
print(random_number)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': 'Home', 'Message': 'loaded page','Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/', methods=['POST'])
def post_req():
    print(random_number)
    data = int(request.get_data(as_text=True))
    if data < random_number:
        data_set = {'Message': 'The number is to low, please try again'}
        json_dump = json.dumps(data_set)
        return json_dump
    elif data > random_number:
        data_set = {'Message': 'The number is to high, please try again'}
        json_dump = json.dumps(data_set)
        return json_dump 
    else:
        data_set = {'Message': 'The number is correct!!!'}
        json_dump = json.dumps(data_set)
        return json_dump
    
app.run(port=7777)
