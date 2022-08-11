from flask_pymongo import PyMongo
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/local"
mongo = PyMongo(app)

@app.route('/register', methods=["POST"])
def reg():
  title = request.form.get('reg-title')
  addr = request.form.get('reg-addr')
  price = request.form.get('reg-price')
  text = request.form.get('reg-text')
  mongo.db['weddinga'].insert_one({
    'title': title,
    'addr': addr,
    'price': price,
    'text': text
  })
  return redirect('/')

@app.route('/')
def index():
  return render_template('list.html')

if __name__ == "__main__":
  app.run()