import sqlite_utils
import llm
from readProp import *
import os

def getCollectionToEmbed(dbName : str,modelName : str,collectionName : str ='FFF2'):
  db = sqlite_utils.Database(dbName)
  embedding_model = llm.get_embedding_model(modelName)
  embedding_model.key = readProperties('OPENAI_KEY')
  collection = llm.Collection(collectionName, db, model=embedding_model)
  return collection

def getDb(dbName):
  db = sqlite_utils.Database(dbName)
  return db

def embed(collection : llm.Collection , data : list):
  collection.embed_multi(data,store=True)  
  
def embed_withmeta(collection : llm.Collection , data : list):
      collection.embed_multi_with_metadata(data,store=True)  

def checkSimilar(collection : llm.Collection , searchStr : str) :
  entries = collection.similar(searchStr,number=5) 
  for entry in entries:
    print(entry.id , entry.content,entry.score)
  return entries

 

