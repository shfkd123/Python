import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', database='python', user='root',
                                     password='java', charset="utf8")
        
        
    def myselect(self):
        ret = []
        curs = self.conn.cursor()
        sql = "select e_id, e_name, birth from emp"
        curs.execute(sql)
        
        rows = curs.fetchall()
        
        for row in rows:
            ret.append({'e_id': row[0], 'e_name': row[1], 'birth': row[2]})
        
        return ret

    def myinsert(self, e_id,e_name,birth):
        curs = self.conn.cursor()
        sql = "INSERT INTO emp (e_id, e_name, birth) VALUES ({}, {}, {})".format(e_id, e_name, birth)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt

    def myupdate(self, e_id,e_name,birth):
        curs = self.conn.cursor()
        sql = "UPDATE emp set e_id = '2', e_name = '3', birth = '3' WHERE e_id = '2'"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def mydelete(self):
        curs = self.conn.cursor()
        sql = "DELETE FROM emp WHERE e_id = 2"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
#    list = de.myselect()
#    print(list)
    
#   cnt = de.myinsert('2', '2', '2')
#    cnt = de.myupdate('2', '3', '3');

    cnt = de.mydelete()
    print(cnt)        
        