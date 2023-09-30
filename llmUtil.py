import sqlite_utils
import llm
from readProp import *
import os

def getCollectionToEmbed(dbName,modelName):
  db = sqlite_utils.Database(dbName)
  embedding_model = llm.get_embedding_model(modelName)
  embedding_model.key = readProperties('OPENAPI_KEY')
  collection = llm.Collection("FFF2", db, model=embedding_model)
  return collection

def embed(collection : llm.Collection , data : list):
  collection.embed_multi(data,store=True)  

def checkSimilar(collection : llm.Collection , searchStr : str) :
  entries = collection.similar(searchStr,number=5) 
  for entry in entries:
    print(entry.id , entry.content,entry.score)
  return entries

 

