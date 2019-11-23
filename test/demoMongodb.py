import pymongo
from bson import json_util as jsonb
client = pymongo.MongoClient("mongodb://192.168.65.119:27017/")
db = client['spider']
col = db['postionCategory']

query = {"nameCategory": "技术"}
import json

#由于python下无法直接处理Object所以这里使用bson对Object进行处理
res=json.dumps(json.loads(jsonb.dumps(col.find(query))))

print(res)

client.close()
