import json
from flask import Flask, request
from markupsafe import escape
from llmUtil import *
from llm import *


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
  db = getDb("fff2.db")
  if Collection.exists(db, "FFF2"):
    ans["collection_exists"] = 'Yes'
  print(f"before sending response {json.dumps(ans)}")
  return ans

@app.route("/checkSimilar",methods=['POST', 'GET'])
def check_similar():
  ans = { }
  search_term = request.form['searchTerm']
  collection = getCollectionToEmbed("fff2.db","ada-002")
# search for term - sign in is supposed to match login
  entries = checkSimilar(collection,search_term)
  ans["similar"] = entries
  return ans
  