import pymysql

class DaoExam:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', database='python', user='root',
                                     password='java', charset="utf8")
        
    def myExamselect(self):
        ret = []
        curs = self.conn.cursor()
        sql = "select e_id, kor, eng, math from exam"
        curs.execute(sql)
        
        rows = curs.fetchall()
        
        for row in rows:
            ret.append({'e_id': row[0], 'kor': row[1], 'eng': row[2], 'math': row[3]})
        
        return ret
    
    def myExaminsert(self,e_id, kor, eng, math):
        curs = self.conn.cursor()
        sql = "INSERT INTO exam (e_id, kor, eng, math) VALUES ({}, {}, {}, {})".format(e_id, kor, eng, math)
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt

    def myExamupdate(self, e_id,e_name,birth):
        curs = self.conn.cursor()
        sql = "UPDATE exam set e_id = '1', kor = '89', eng = '99', math = '100' WHERE e_id = '1'"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def myExamdelete(self):
        curs = self.conn.cursor()
        sql = "DELETE FROM exam HERE e_id = 1"
        cnt = curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoExam()
#    list = de.myExamselect()
#    print(list)
    
#    cnt = de.myExaminsert('2', '99', '58', '77')
#    cnt = de.myExamupdate('2', '3', '3');

#    cnt = de.myExamdelete()
#    print(cnt)        
    