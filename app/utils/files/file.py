import os
from json import dump, loads

scriptDir = os.path.dirname(os.path.abspath(__file__))
destination = os.path.join(scriptDir, '..', '..', 'data')

def createFile(name, ext, data):
    try: os.makedirs(destination)
    except OSError: pass

    path = os.path.join(destination, f'{name}.{ext}')
    with open(path, 'w') as file:
        if(ext == 'json'): dump(data, file, indent=4)
        else: file.write(data)
        print(f'{name} file updated')
    
def readFile(name, ext):
    try:
        path = os.path.join(destination, f'{name}.{ext}')
        with open(path, 'r') as file: 
            return loads(file.read())[name]
    except:
        return False