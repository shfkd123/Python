from flask import Flask, jsonify, render_template, request 
import os
import sys
import urllib.request

app = Flask(__name__)

@app.route('/')
def call_API():
    return render_template('capcha.html') 

@app.route('/key')
def getKey():
    client_id = "myfl5dAv37u_QhegWA7y"
    client_secret = "4x6VUgzS0w"
    code = "0"
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
    
@app.route('/image')
def getImage():
    key = request.args.get('imgkey')
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    return url

@app.route('/compare')  
def compare():
    client_id = "myfl5dAv37u_QhegWA7y"
    client_secret = "4x6VUgzS0w"
    code = "1"
    key = request.args.get('imgkey')
    value = request.args.get('value')
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        
if __name__ == '__main__':
        app.run(debug=True)