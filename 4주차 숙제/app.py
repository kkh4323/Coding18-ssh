from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/detail')
def detail():
  collection = mongo.db.dangdang
  _title = request.args.get('title')
  product = collection.find_one({"title": _title})
  res = jsonify({
    'title': product.get('title'),
    'text': product.get('text')
  })
  return res

@app.route('/register', methods=["POST"])
def reg():
  title = request.form.get('reg-title')
  addr = request.form.get('reg-addr')
  price = request.form.get('reg-price')
  text = request.form.get('reg-text')
  mongo.db['dangdang'].insert_one({
    'title': title,
    'addr': addr,
    'price': price,
    'text': text
  })
  return redirect('/')

@app.route('/')
def index():
  itemList = mongo.db['dangdang'].find()

  return render_template('list.html', itemList=itemList)

if __name__ == "__main__":
  app.run()