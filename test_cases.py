from readProp import * 
from data import *
from llmUtil import *

# read the embedding from database 
collection = getCollectionToEmbed("fff2.db","ada-002")
# search for term - sign in is supposed to match login
entries = checkSimilar(collection,"sign in")