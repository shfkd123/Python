from flask import Flask
from flask import request
from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return "hello, world!"

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)