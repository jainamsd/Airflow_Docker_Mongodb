import pymongo

url=pymongo.MongoClient("mongodb+srv://DATABASE:PASSWORD@cluster0.p688c.mongodb.net/")
db=url["automation_config"]
collection=db["config"]

execute_query=collection.find({})
print("convert value----->"+str(list(execute_query)))
# for index in execute_query:
#     print(index)