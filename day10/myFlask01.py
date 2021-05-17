from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/')
def home():
    a = request.args.get('a', "하하하") ##데이터가 안들어면 default로 '하하하'를 받음
    return 'Hello, {}'.format(a)

if __name__ == '__main__':
    app.run(debug=True)