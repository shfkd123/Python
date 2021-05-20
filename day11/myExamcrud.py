from flask import Flask,render_template, jsonify, request
from day11.mydao_exam import DaoExam

app = Flask(__name__,static_url_path='')

@app.route('/')
@app.route('/list')
def list():
    de = DaoExam()
    mylist = de.myExamselect()
    return render_template('list2.html',mylist=mylist)


@app.route('/add.ajax', methods=['POST'])
def ajax_add():
    p = request.get_json()
    de = DaoExam()    
    cnt = de.myExaminsert(p['e_id'],p['kor'],p['eng'],p['math'])
    msg = ""
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/del.ajax', methods=['POST'])
def ajax_del():
    p = request.get_json()
    de = DaoExam()
    cnt = de.myExamdelete(p['e_id'])
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
    
    return jsonify(msg = msg)

@app.route('/upd.ajax', methods=['POST'])
def ajax_upd():
    p = request.get_json()
    de = DaoExam()
    cnt = de.myExamupdate(p['e_id'],p['kor'],p['eng'],p['math'])
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else :
        msg = "ng"
    
    return jsonify(msg = msg)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    