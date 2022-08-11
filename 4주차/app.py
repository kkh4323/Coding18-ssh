from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello_world.html')

@app.route('/fc')
def fastcampus():
    res = []
    for i in range(10):
      res.append(
        {"title": f"{i}title"}
      )
    return jsonify(res)

if __name__ == '__main__': # import 되지 않고 직접 실행할 때만 작동시키는 함수
    app.run()              # 직접 실행하면 '__main__'으로 나오지만 import하면 파일명이 나옴.