#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def readFiles(path):
    
    """
        Load the model and feature
    """
    
    filePath='/' + path + '/'   #load json and create model
    
    
    filePathModel = filePath + 'model.json'
    json_file = open(filePathModel, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    filePathWeight=filePath+'model.h5'
    loaded_model.load_weights(filePathWeight)
    print("Loaded model from disk")

    ## open file and read the content in a list
    filePathColumn=filePath+'column.txt'
    columns = []
    with open(filePathColumn, 'r') as filehandle:
        columns = [c.rstrip() for c in filehandle.readlines()]

    #load scaler
    filePathScaler=filePath+'scaler.sav'
    loaded_scaler = pickle.load(open(filePathScaler, 'rb'))

    ## open file and read the content in a list
    filePathThreshold=filePath+'threshold.txt'
    with open(filePathThreshold, 'r') as filehandle:
        threshold=float(filehandle.read())
        
    return loaded_model,columns,loaded_scaler,threshold

