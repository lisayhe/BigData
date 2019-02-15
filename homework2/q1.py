#!/apps/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 14:54:46 2019

@author: Lisa He
"""

import pandas as pd
import numpy as np

missing_values = ["Null", "?", "--","","FALSE",".","-","nan","False","R","r"]
pd_file = pd.read_csv('./monthly_returns_mv.csv', na_values = missing_values)

funds = np.unique(pd_file.loc[:, ['crsp_fundno']])
    
for f in funds:
    temp = pd_file[pd_file['crsp_fundno']==f] 
    if len(temp)>1:
        temp2 = pd_file[pd_file['crsp_fundno']==f].interpolate()
        pd_file[pd_file['crsp_fundno']==f] = temp2
        
pd_file.to_csv('q1result.csv')