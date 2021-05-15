import os
import sys
import urllib.request
client_id = "myfl5dAv37u_QhegWA7y" # 개발자센터에서 발급받은 Client ID 값
client_secret = "4x6VUgzS0w" # 개발자센터에서 발급받은 Client Secret 값
key = "b1o5UQoMC74Ffsdf" # 캡차 Key 값
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
else:
    print("Error Code:" + rescode)