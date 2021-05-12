import os
import sys
import urllib.request
from bs4 import BeautifulSoup
from _datetime import datetime
import pymysql
import time

#아래 문단을 아래쪽에 위치하면 안됨. 
def insertStock(tuts):
    conn = pymysql.connect(host='localhost', user='root', password='java',
                           db='python', charset='utf8')
    
    curs = conn.cursor()
    sql = "INSERT INTO stock (s_code, s_name, s_price, crawl_date) VALUES (%s, %s, %s, %s)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

for i in range(10):
    url = "https://vip.mk.co.kr/newSt/rate/item_all.php"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        html = response_body.decode('euc-kr')
        soup = BeautifulSoup(html, 'html.parser')
        
        now = datetime.now()
        crawl_date = now.strftime("%Y%m%d.%h%m")
        tuts = []
        
        items = soup.select(".st2")
        for i, item in enumerate(items):
            s_code = item.a['title']
            s_name = item.text
            s_price = item.parent.select('td')[1].text.replace(",","")
            
            tuts.append((s_code, s_name, s_price, crawl_date))
        
        cnt = insertStock(tuts)
        print("cnt", cnt)
    
    else:
        print("Error Code:" + rescode)    

    time.sleep(60)