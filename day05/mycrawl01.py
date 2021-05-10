import requests
from bs4 import BeautifulSoup

url = 'http://localhost/CRAWL/crawl.html'

response = requests.get(url) #get방식

if response.status_code == 200: #서버 정상 200
    html = response.text
    #print(html) #html을 text 형태로 출력
    soup = BeautifulSoup(html, 'html.parser') #html을 parsing
    
    print("선생님 풀이")
    tds = soup.select("td")
    for i,td in enumerate(tds):
        if i > 1:
            print(td.get_text())
    
    print("-------------------------------")
    for td in soup.find_all('td'):
        print(td.get_text())
    

else : 
    print(response.status_code)