import pickle
import logging
import re

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
    
    
def loadAndTokenize(testFile):
    logging.debug(f'loading a test file {testFile} ')
    f = open(testFile, "r")
    l = 0
    testSection = None
    list_content = []
    for x in f:
      l += 1
      metadata = {}
      metadata["line_no"] = l
      metadata['file_name'] = testFile
      print(x)
      (id,content)= processLine(x,testSection)
      print(f" id {id} content {content}")
      if id == None and content == None :
        continue
      elif content == None or content =='':
        testSection = id   
    
      if(content != None):
        list_content.append((id,content,metadata))
    
    print(f' line count {l}')
    print (*list_content, sep="\n")
    

#loadATestScript('Test009BlocksAndModels.rhino')


#{{$ --user:open-project user name --password:open-project password}} on {element} using {css selector} from {attribute} filter {regex}
def processArguments(content:str):
  """
  this function looks for arguments and tries to make it 
  english sentences for arguments for NLP processor 
  replacement text = with argument user = new user and password = new password     
  """ 
  print(f"processArgument {content}")
  repl = content
  if(content.find("{{") != -1):
    args_list = content.split("}}")
    args = args_list[0]
    new_args = args.split("{{")
    prefix = new_args[0]
    repl = prefix + ' using arguments'
    repl = repl + re.sub('\$'  ," ",new_args[1])
    repl = re.sub(":","=",repl)
    repl = re.sub("--","AND ",repl)
    repl=repl.lstrip()
    repl = re.sub("AND","",repl,1)
    if(len(args_list) > 1):
      remain_str = args_list[1]
      remain_str = re.sub("{","",remain_str) 
      remain_str = re.sub("}","",remain_str) 
      repl = repl + remain_str      
  return repl

def processLine(line : str,testSection : str):
   """
   this function parses a line in test rhino script 
   each line will have test-*** , which denotes section 
   and action for that test section 
   blank lines to be ignored
   lines which starts with numeric number , will have test section concatenated
   """
   id = None
   content = None
   repl = None
   print(line)
   if(line.strip().startswith("[") ):
      list = line.split("]")
      id = list[0]
      id=id.strip("[")
      content = list[1].strip()
      repl = content
   else:
      lineNo = line[0:1]
      if (lineNo.isdigit()):
        id = testSection + "-" + line.split(".")[0]
        content =  line.split(".")[1].strip()
        repl = processArguments(content)
    
   return (id ,repl)
    
loadAndTokenize('Test009BlocksAndModels.rhino')


