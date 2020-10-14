from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['MICROV2']

shop_col = db['testShop']

shops_cursor = shop_col.find()

for shop in shops_cursor:
    if shop['shopType'] == 'reseller':
        shop_col.update_one({'_id': shop['_id']}, { "$set": { "description": shop['description']+" updated" } })
        print(shop)
    # print(shop)


