import pymysql

conn = pymysql.connect(host='localhost', database='python', user='root', password='java', charset="utf8")
try:
    curs = conn.cursor()
    sql = "delete from hello where col01 = 1"
    curs.execute(sql)
    conn.commit()

finally:
    conn.close()