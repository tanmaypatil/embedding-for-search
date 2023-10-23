import json
from flask import Flask, request
from markupsafe import escape
from llmUtil import *
from llm import *
from store import * 
from readProp import *
embed_db = readProperties("EMBED_DB")


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def print_name(name):
    return f"Hello, {escape(name)}!"

@app.route("/embeddingExist")
def embedding_exists():
  ans = {}
  ans["collection_exists"] = 'No'
  db = getDb(embed_db)
  if Collection.exists(db, "FFF2"):
    ans["collection_exists"] = 'Yes'
  print(f"before sending response {json.dumps(ans)}")
  return ans

@app.route("/checkSimilar",methods=['POST', 'GET'])
def check_similar():
  ans = { }
  search_term = request.form['searchTerm']
  collection = getCollectionToEmbed(embed_db,"ada-002")
# search for term - sign in is supposed to match login
  print(f"searching for {search_term}")
  entries = checkSimilar(collection,search_term)
  ans["similar"] = entries
  return ans

@app.route("/deleteEmbedding",methods=['POST'])
def delete_embedding():
  collection_name = request.form['collectionName']
  ans = {}
  ans["collectionExisted"] = 'No'
  db = getDb(embed_db)
  if Collection.exists(db, collection_name):
    ans["collectionExisted"] = 'Yes'
    collection = getCollectionToEmbed(embed_db,"ada-002")
    collection.delete()
    ans["collectionDeleted"] = 'Yes'  
  print(f"before sending response {json.dumps(ans)}")
  return ans

@app.route("/addEmbedding",methods=['POST'])
def add_embedding():
  ans = {}
  file_name = request.form["fileName"]
  meta_reqd = request.form["metaRequired"]
        
  embedding_list = loadAndTokenize(file_name,meta_required=meta_reqd) 
  collection = getCollectionToEmbed(embed_db,"ada-002",'FFF2')
  if(meta_reqd == 'Yes'):
    embed_withmeta(collection,embedding_list)
  else:
    embed(collection,embedding_list)
    
  db = getDb(embed_db)
  if Collection.exists(db, "FFF2"):
      ans["collectionCreated"] = 'Yes'
  return ans
  
  