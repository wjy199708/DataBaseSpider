import json

f = open('./data/demojson.txt', encoding='utf-8')
x = json.load(f)
x = str(x)
print(x)
