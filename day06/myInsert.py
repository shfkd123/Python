import pymysql

def insertChicken(tuts):
    
    conn = pymysql.connect(host='localhost', database='python', user='root', password='java', charset="utf8")
    
    curs = conn.cursor()
    sql = "INSERT INTO HELLO (COL01, COL02, COL03) VALUES (%s, %s, %s)"
    cnt = curs.executemany(sql, tuts)
    
    conn.commit()
    conn.close()
    return cnt

if __name__== '__main__':
    tuts = []
    tuts.append(('4','1','1'))
    tuts.append(('5','2','2'))
    tuts.append(('6','3','3'))
    cnt = insertChicken(tuts)
    print("cnt", cnt)