import db
import os
from dotenv import load_dotenv
load_dotenv()
db.host = os.getenv("HOST")
db.user = os.getenv("USER")
db.password = os.getenv("PASSWORD")
db.database = os.getenv("DATABASE")

with open('слова.txt', 'r',encoding='utf-8') as f:
    myList = [ line.split() for line in f ]


flatList = [item for sublist in myList for item in sublist]
for i in range(len(myList)):
    word = myList[i][1]
    db.request_not_return(f"INSERT INTO words (word) VALUES ('{word}')")
    print(myList[i][0])
