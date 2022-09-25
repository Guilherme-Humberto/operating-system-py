from app.utils.files import file

def registerModel(modelKey, modelData, payload):
    if(len(modelData[modelKey]) == 0):
        file.createFile(modelKey, 'json', {modelKey: modelData[modelKey]})

    hasModelData = (
        len(modelData[modelKey]) > 0 
        and 'item' in modelData.keys() 
        and len(modelData['item']) >= 1
    )
    
    if(hasModelData and len(modelData['item']) >= 1): 
        raise ValueError(f'{modelKey} already exists')

    modelData[modelKey].append(payload)
    file.createFile(modelKey, 'json', {modelKey: modelData[modelKey]})