import pickle
import logging

def addRecord(id : str , content :str , metadata :dict, list : list) :
    logging.debug(f'{id} adding a line into record')
    record = ( id , content, metadata)
    list.append(record)

def saveFile(list,filename):
    with open(filename, 'wb') as filehandle:
      pickle.dump(list,filehandle)

def loadASerialisedFile(filename):
    logging.debug(f'loading a picked file {filename} reading into list')
    with open(filename, 'rb') as filehandle:
      list = pickle.load(filehandle)
      return list

def loadATestScript(testFile):
    logging.debug(f'loading a test file {testFile} ')
    f = open(testFile, "r")
    l = 0
    for x in f:
      l += 1
      print(x)
    
    print(f' line count {l}')
    

loadATestScript('Test009BlocksAndModels.rhino')

def processLine(line : str,testSection : str):
   """
   this function parses a line in test rhino script 
   each line will have test-*** , which denotes section 
   and action for that test section 
   blank lines to be ignored
   lines which starts with numeric number , will have test section concatenated
   """
   id = ''
   content = ''
   if(line.strip().startswith("[") ):
      list = line.split("]")
      id += list[0]
      id=id.strip("[")
      content = list[1].strip()
   else:
      lineNo = line[0:1]
      if (lineNo.isdigit()):
        id += testSection + line
    
   return (id ,content)
    



