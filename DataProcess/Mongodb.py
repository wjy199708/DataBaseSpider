import pymongo
import DataProcess.setting as setting


def StorageData(collections_name, data):
    uri = setting.MongoDb_Url
    # 创建连接对象
    client = pymongo.MongoClient(uri)
    db = client[setting.Mongodb_Db]
    db[collections_name].insert_one(dict(data))
    print("mongo插入的此次一条数据为：：{0}".format(dict(data)))
    client.close()

# StorageData('java', {'name': 'java', 'age': '10'})
