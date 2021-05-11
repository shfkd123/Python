import pymysql

conn = pymysql.connect(host='localhost', database='python', user='root', password='java', charset="utf8")

try:
    curs = conn.cursor()
    sql = "update hello set col02 = '2', col03 = '2' where col01 = 1"
    cnt = curs.execute(sql)
    print("cnt", cnt)
    conn.commit()

finally:
    conn.close()