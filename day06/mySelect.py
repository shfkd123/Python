import mysql.connector

conn = mysql.connector.connect(host='localhost ', database='python', user='root', password='java', charset="utf8")
try :
    curs = conn.cursor()
    sql = "select * from hello"
    curs.execute(sql)
    rows = curs.fetchall()
    
    for row in rows:
        print(row)
finally:
    conn.close()