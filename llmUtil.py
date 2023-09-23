import sqlite_utils
import llm
from readProp import *

def getCollectionToEmbed(dbName,modelName):
  db = sqlite_utils.Database(dbName)
  embedding_model = llm.get_embedding_model(modelName)
  embedding_model.key = read_properties('OPENAPI_KEY')
  collection = llm.Collection("entries", db, model=embedding_model)
  return collection