import os
import sys
import urllib.request
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
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)