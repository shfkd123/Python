from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    a = request.form.get('a', "하하하")
    return 'Hello {}'.format(a)
if __name__ == '__main__':
    app.run(debug=True)  