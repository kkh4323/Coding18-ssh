from pymongo import MongoClient
import requests as rs                                        # as는 긴 라이브러리 명을 임의로 설정할 수 있게 함.
from bs4 import BeautifulSoup as bs
from pymongo.mongo_client import MongoClient as mc

client = mc("mongodb://localhost:27017/")
db = client.local
collection = db.yes25

rows = collection.find() # collection의 값들을 list로 반환(Cursor랑 list랑 비슷한거) list = ['a', 'b', 'c']
for row in rows:         # 생성된 list를 한 줄 씩 불러옴.
  print(row['title'])    # 불러온 한 줄의 value값을 key값을 통해 불러옴. 'title'은 string값. title어떤 타입인지 모름. 

# res = rs.get("http://www.yes24.com/24/Category/BestSeller")  # 주소를 가져옴.
# soup = bs(res.text, "html.parser")                           # 값을 예쁘게 바꿔줌. 인식하기 쉽게?

# for i in range(40):
#   idx = str(i + 1)
#   if idx == "19":
#     idx = "19_line"
#   elif idx == "20":
#     idx = "20_line"
#   elem = soup.select_one(f'#bestList > ol > li.num{idx} > p:nth-child(3) > a')
#   db['yes25'].insert_one({'title':elem.text}) # key 값을 통해 value 값을 불러옴
