# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pymysql
from bs4 import BeautifulSoup
import requests

def insertChicken(tuts):
    
    conn = pymysql.connect(host='localhost', database='python', user='root', password='java', charset="utf8")
    
    curs = conn.cursor()
    sql = "INSERT INTO STOCK (s_code, s_name, s_price, crawl_date) VALUES (%s, %s, %s, SYSDATE)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    html = response_body.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.select("item")
    for i,item in enumerate(items):
        print(item.title.text)
        print()
        print(item.description.text)
        print()
        print()
    
    
else:
    print("Error Code:" + rescode)