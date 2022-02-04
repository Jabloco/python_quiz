from pymongo import MongoClient

from constants import MONGODB_HOST, MONGODB_PORT


client = MongoClient(MONGODB_HOST, MONGODB_PORT)

db = client.quiz

doc_users = db.users
doc_questions = db.questions
