import pymongo
import json


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["courses"]
collection = db["courses"]

with open("courses.json", mode="r") as file_reader:
    courses = json.load(file_reader)


collection.create_index("name")

for course in courses:
    course["rating"] = {"total": 0, "count": 0}

for course in courses:
    for chapter in course["chapters"]:
        chapter["rating"] = {"total": 0, "count": 0}
    
for course in courses:
    collection.insert_one(course)

client.close()




