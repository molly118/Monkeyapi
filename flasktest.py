# coding=utf-8

from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/')
def home():
    data = json.dumps({
        'username': 'yuanwang',
        'password': 'yuanwang1'
    })

    return data


@app.route('/api/v2/auth/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = json.dumps({
            'username': username,
            'password': password,
            'code': 200,
            'message': 'login'
        })
    else:
        data = json.dumps({
            'message': 'input username or password'
        })
    return data


@app.route('/api/v2/auth/post_login', methods=['POST'])
def post_login():
    r_method = request.method
    if r_method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        data = json.dumps({
            'username': username,
            'password': password,
            'code': 200,
            'message': 'login'
        })
    else:
        data = json.dumps({
            'message': 'input username or password'
        })
    return data





#http://test.monkey.cool/api/v2/auth/login

if __name__ == '__main__':
    app.run()
