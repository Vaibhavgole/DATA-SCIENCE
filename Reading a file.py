import osSkip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@ajinkya48765 
1
00Vaibhavgole/DATA-SCIENCE
 Code Issues 0 Pull requests 0 Actions Projects 0 Wiki Security Insights
You’re editing a file in a project you don’t have write access to. We’ve created a fork of this project for you to commit your proposed changes to. Submitting a change to this file will write it to a new branch in your fork, so you can send a pull request.
DATA-SCIENCE
/
Reading a file
 

1
import os
2
FilePath = "/home/vaibhavgole/Desktop"
3
os.chdir(FilePath)
4
import numpy as np
5
import pandas as pd
6
file = pd.read_excel("TeachersFileFormat.xlsx", index =3,axis=0, na_values = " ", sheet_name = "Sheet1")
7
data=file.copy(deep=1)
8
​
9
shape=data.shape
10
rows=shape[0]
11
columns=shape[1]
12
col_name=data.columns
13
a=data.isna().sum()
14
​
15
for i in range(0,len(a),1):
16
    if(a[i]==rows or a[i]==rows-1):
17
        data = data.drop(col_name[i],axis=1)
18
        
19
​
20
missing=data[data.isna().any(axis=1)]
21
missingIndex=missing.index
22
print(len(missingIndex))
23
​
24
for e in range(0,len(missingIndex),1):
25
    data = data.drop(missingIndex[e],axis=0)
26
    
27
print(len(data["Unnamed: 1"]))
28
​
@ajinkya48765
Propose file change
Commit summary
Update Reading a file
Optional extended description
Add an optional extended description…
 
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About

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
