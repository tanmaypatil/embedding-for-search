from readProp import * 
from data import *
from llmUtil import *
value = read_properties('OPENAPI_KEY')
print(data)

collection = getCollectionToEmbed("fff2.db","ada-002")
entries = checkSimilar(collection,"sign in")