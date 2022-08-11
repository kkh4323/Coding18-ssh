import datetime, math
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/write', methods=["POST"])
def write():
  name = request.form.get('name')
  content = request.form.get('content')
  mongo.db['wedding'].insert_one({
    'name': name,
    'content': content
  })
  return redirect('/')

@app.route('/') 
def index():
  now = datetime.datetime.now()
  wedding = datetime.datetime(2022, 8, 18, 0, 0, 0)
  diff = (wedding - now).days

  page = int(request.args.get('page', 1))   # page값을 받아오고, 받아오는 값이 없으면 1을 반환
  limit = 3                                 # 한 페이지 당 3줄씩 불러오기로 함
  skip = (page - 1) * limit                 # 한 페이지 당 3줄씩이니 다음 페이지에선 앞의 3줄이 생략되어야 함.

  count = mongo.db['wedding'].count_documents({}) # wedding 컬렉션의 데이터 갯수를 센다.
  max_page = math.ceil(count / limit)             # math 패키지의 ceil 함수를 이용해 값을 올림 처리한다.
  pages = range(1, max_page + 1)

  guestbooks = mongo.db['wedding'].find().limit(limit).skip(skip)


  return render_template('index.html', diff=diff, guestbooks=guestbooks, pages=pages) # 주머니 = 값.

if __name__ == "__main__":
  app.run()