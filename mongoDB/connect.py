from pymongo import MongoClient

client = MongoClient()

db = client.catalogue

book = {"title": "A light in the Arttic"}

students = db.books

document_id = students.insert_one(book).inserted_id
print(document_id)

documents = [
    {
        "title": "A Light in the Attic",
    },
    {
        "title": "Tipping the Velvet",
    },
    {
        "title": "Soumission",
    },
]

students.insert_many(documents)

print(students.find_one())

for book in students.find({"title": {"$regex": "t"}}):
    print(book["title"])

client.close()
