from jproperties import Properties

def read_properties(key):
   configs = Properties()
   with open('app.properties', 'rb') as config_file:
     configs.load(config_file)
   print(f'Database User: {configs.get(key).data}') 
   return configs.get(key).data
