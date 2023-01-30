#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import tensorflow
from tensorflow import keras


def load_model():
    
    dir_location = os.path.join(os.path.dirname(__file__), 'Model')
    
    #Load model
    model = keras.models.load_model(dir_location)
    
    return model


# In[ ]:




