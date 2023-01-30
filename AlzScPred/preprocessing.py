#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

def preprocess_data(df):
    
    # Removing all the cells with zero values in it.i.e. all the rows have zero in it.
    
    df= df.loc[(df!=0).any(axis=1)]
    
    #df1 = df.loc[:,(df==0).mean()<0.8] ## removing all the columns with more than 80 % zeroes 
    
    selected_genes = ['ARL17B', 'NAIP', 'BCOR', 'XIST', 'TSC22D4', 'HEPACAM', 'FGF17', 'EZH1', 'FOXN2', 'NDUFAF6', 'CC2D1A', 'MARCKSL1', 'ZDHHC11B', 'PLXNB1', 'PLPPR2', 'AC090517.4', 'CDK18', 'LGI4', 'CHD7', 'RBMX', 'CDKL1', 'DNAJC7', 'SLC25A13', 'PER1', 'LPAR1', 'HIBADH', 'ZBED5', 'PTDSS2', 'ATG4B', 'PWWP2A', 'XRRA1', 'OTUD7B', 'SCD', 'UBE2Z', 'PIGQ']
    
    df1 = df[selected_genes]
    
    return df1

