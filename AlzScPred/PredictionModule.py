#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tensorflow 
from tensorflow import keras


def predict_patient(model,file):
    
    y_pred = model.predict(file)
    
    predictions = list(map(lambda x: 0 if x<0.5 else 1, y_pred))
    
    ones =0
    zeros =0
    
    for i in range(len(predictions)):
        if (predictions[i]==1):
            ones +=1
        else:
            zeros+=1
            
    #print("The number of ones are ", ones)
    #print("The number of zeros are ", zeros)
    #print("Total number of cells are ", len(predictions))
    print("Predicted percentage of Diseased cells are ", ones/len(predictions))
    print("Predicted percentage of Normal cells are ", zeros/len(predictions))
    
    op= ones/len(predictions) 
    zp= zeros/len(predictions)
    
    if(op>0.45):
        print("Alzheimer's patient detected")
        print("More than 45% diseased cells found")
    else:
        print("Normal patient found, No disease detected")

