import os 

def readCodeStr(funcName):
  cmdLine = 'symbex '+funcName
  code = os.popen(cmdLine).read()
  return code

def readContinueCode():
  functionName = 'readProperties'
  while (functionName != 'end_function') : 
    functionName = input("Enter function name , write end_function to finish :")
    code = readCodeStr(functionName)
    print(code)
  print('exiting forever loop')