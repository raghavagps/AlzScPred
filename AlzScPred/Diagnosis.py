import os
import pandas as pd
import tensorflow 
from tensorflow import keras

def predict_patient(df):

  # Removing all the cells with zero values in it.i.e. all the rows have zero in it.
      
  df= df.loc[(df!=0).any(axis=1)]
      
  #df1 = df.loc[:,(df==0).mean()<0.8] ## removing all the columns with more than 80 % zeroes 
      
  selected_genes = ['ARL17B', 'NAIP', 'BCOR', 'XIST', 'TSC22D4', 'HEPACAM', 'FGF17', 'EZH1', 'FOXN2', 'NDUFAF6', 'CC2D1A', 'MARCKSL1', 'ZDHHC11B', 'PLXNB1', 'PLPPR2', 'AC090517.4', 'CDK18', 'LGI4', 'CHD7', 'RBMX', 'CDKL1', 'DNAJC7', 'SLC25A13', 'PER1', 'LPAR1', 'HIBADH', 'ZBED5', 'PTDSS2', 'ATG4B', 'PWWP2A', 'XRRA1', 'OTUD7B', 'SCD', 'UBE2Z', 'PIGQ']
      
  df1 = df[selected_genes]


  # Load the model

  dir_location = os.path.join(os.path.dirname(__file__), 'Model')
      
  #Load model
  model = keras.models.load_model(dir_location)



  y_pred = model.predict(df1)
      
  predictions = list(map(lambda x: 0 if x<0.5 else 1, y_pred))
      
  ones = 0
  zeros =0
      
  for i in range(len(predictions)):
      if (predictions[i]==1):
          ones +=1
      else:
          zeros+=1
              
  #print("The number of ones are ", ones)
  #print("The number of zeros are ", zeros)
  #print("Total number of cells are ", len(predictions))
  #print("Predicted percentage of Diseased cells are ", (ones/len(predictions))*100)
  #print("Predicted percentage of Normal cells are ", (zeros/len(predictions))*100)
      
  op= ones/len(predictions) 
  zp= zeros/len(predictions)
      
  if(op>0.45):
      print("Alzheimer's patient detected")
      print("More than 45% diseased cells found")
      print("Patient found to be having {} percentage of diseased cells" .format(op*100))
  else:
      print("Normal patient found, No disease detected")
      print("{} percentage Normal cells found" .format(zp*100))


