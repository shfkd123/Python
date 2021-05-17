import os
import sys
import urllib.request
import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/captcha_key')
def captcha_key():        
    client_id = "myfl5dAv37u_QhegWA7y" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "4x6VUgzS0w" # 개발자센터에서 발급받은 Client Secret 값
    code = "0"
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        capcha_key = response_body.decode('utf-8')
        #print("캡챠 키 : "+ capcha_key)
        jsonObject = json.loads(capcha_key)
        key_value = jsonObject.get("key");
        print(key_value)

        return captcha_img(key_value)
    
    else:
        print("Error Code:" + rescode)

@app.route('/captcha_img', methods=['POST'])
def captcha_img(key_value):
    client_id = "myfl5dAv37u_QhegWA7y" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "4x6VUgzS0w" # 개발자센터에서 발급받은 Client Secret 값
    key = key_value # 캡차 Key 값
    url = "https://openapi.naver.com/v1/captcha/ncaptcha.bin?key=" + key
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        print("캡차 이미지 저장")
        response_body = response.read()
        with open('captcha.jpg', 'wb') as f:
            f.write(response_body)
        
        #return captcha_user(key_value, value) 
    else:
        print("Error Code:" + rescode)
        
@app.route('/captcha_user')
def captcha_user(key_value):
    client_id = "myfl5dAv37u_QhegWA7y" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "4x6VUgzS0w" # 개발자센터에서 발급받은 Client Secret 값
    code = "1"
    key = key_value
    value = ""
    url = "https://openapi.naver.com/v1/captcha/nkey?code=" + code + "&key=" + key + "&value=" + value
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
        

if __name__ == "__main__":
    captcha_key()      