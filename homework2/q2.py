#!/apps/anaconda3/bin/python
# -*- coding: utf-8 -*-
#Lisa He
import numpy as np
import pandas as pd


missing_values = ["Null", "?", "--","","FALSE",".","-","nan","False","R","r"]
pd_file = pd.read_csv('./monthly_returns_mv.csv', na_values = missing_values)


funds = np.unique(pd_file.loc[:, ['crsp_fundno']])

split_funds = [funds[i*4775:(i+1)*4775] for i in range(10)]

result_funds = pd.DataFrame(columns= pd_file.columns)

import sys
job = int(sys.argv[1])-1
funds_to_run = split_funds[job]

for f in funds_to_run:
    temp = pd_file[pd_file['crsp_fundno']==f] 
    temp2 = temp.interpolate()
    
   # assert(temp2.shape[1] == len(pd_file.columns))
    result_funds = result_funds.append(pd.DataFrame(temp2),ignore_index=True)
        #d_file[pd_file['crsp_fundno']==f] = temp2
    
    print(f,'\n')
#result_funds.append(pd_file)        

        
result_funds.to_csv('gridresult.csv')