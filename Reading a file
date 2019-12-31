import os
FilePath = "/home/vaibhavgole/Desktop"
os.chdir(FilePath)
import numpy as np
import pandas as pd
file = pd.read_excel("TeachersFileFormat.xlsx", index =3,axis=0, na_values = " ", sheet_name = "Sheet1")
data=file.copy(deep=1)

shape=data.shape
rows=shape[0]
columns=shape[1]
col_name=data.columns
a=data.isna().sum()

for i in range(0,len(a),1):
    if(a[i]==rows or a[i]==rows-1):
        data = data.drop(col_name[i],axis=1)
        

missing=data[data.isna().any(axis=1)]
missingIndex=missing.index
print(len(missingIndex))

for e in range(0,len(missingIndex),1):
    data = data.drop(missingIndex[e],axis=0)
    
print(len(data["Unnamed: 1"]))
