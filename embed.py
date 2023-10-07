from readProp import * 
from data import *
from llmUtil import *
value = readProperties('OPENAPI_KEY')
#print(data)

collection = getCollectionToEmbed("fff2.db","ada-002")
embed(collection=collection,data=data)
entries = checkSimilar(collection,"chrome")





