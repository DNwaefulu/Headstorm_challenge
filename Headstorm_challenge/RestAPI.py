from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json, sys

app = Flask(__name__)

Name = input("Enter filename: ")

#Write file
def write(numbers):
    with open(Name, 'w') as write_file:
        json.dump(numbers, write_file)

#Read file
def read(numbers):
    with open(Name, 'r') as read_file:
        json.dump(read_file)

#Enact post method to determine if there is 500 numbers
@app.route('/data', methods=['POST'])
def post():
    numbers = request.json
    
    if (len(numbers) != 500):
        sys.exit("Error: The list has to be exactly 500 numbers")
    
    numbers.sort()
    write(numbers)
    
#Enact get method to sort the numbers in order from least to greatest
@app.route('/data', methods=['GET']) 
def get():
    numbers = read()
    return jsonify(numbers)

if __name__=="__main__":
    app.run(debug=True)