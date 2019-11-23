import redis

client = redis.Redis(host='192.168.65.119', charset='utf-8')
x=client.get("lagou:namcategory:技术:测试")

x=client.get("lagou:产品:产品经理")

print(type(x))
