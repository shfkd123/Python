# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import requests
from bs4 import BeautifulSoup
import pymysql
from docutils.nodes import title
from conda.core import link
from astroid.__pkginfo__ import description

def insertChicken(tuts):
    
    conn = pymysql.connect(host='localhost', database='python', user='root', password='java', charset="utf8")
    
    curs = conn.cursor()
    sql = "INSERT INTO CHICKEN (title, link, description, blogname, bloglink, postdate) VALUES (%s, %s, %s, %s, %s, %s)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

client_id = "f4fbpPBChc_CAKtroyjS"
client_secret = "d37hKYSHdx"
encText = urllib.parse.quote("치킨")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'xml') #html을 parsing
    
    items = soup.select("item")
    tuts = []
    for i,item in enumerate(items):
        title       = item.title.text
        link        = item.link.text 
        description = item.description.text 
        blogname    = item.bloggername.text 
        bloglink    = item.bloggerlink.text 
        postdate    = item.postdate.text 
        
        tuts.append((title, link, description, blogname, bloglink, postdate))
    
    cnt = insertChicken(tuts)
    print("cnt", cnt)
    
else:
    print("Error Code:" + rescode)