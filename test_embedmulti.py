from data3 import embedding_list
from llmUtil import *


collection = getCollectionToEmbed("fff2.db","ada-002",'FFF2')
embed_withmeta(collection,embedding_list)