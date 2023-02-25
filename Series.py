# pandas.Series( data, index, dtype, copy)
import pandas as pd 
print(pd.Series()) # Series([], dtype: float64)

s=pd.Series(["Raja","Anbu","Siva"])
print(s)
"""
0    Raja
1    Anbu
2    Siva
"""

s=pd.Series(["Raja","Anbu","Siva"],index=["A","B","C"])
print(s)
"""
A    Raja
B    Anbu
C    Siva
"""


data=[{"Name":"Raja","Age":23},{"Name":"Anbu","Age":22}]
s=pd.Series(data)
print(s)
"""
0    {'Name': 'Raja', 'Age': 23}
1    {'Name': 'Anbu', 'Age': 22}
"""


data={"Name":"Raja","Age":23}
s=pd.Series(data)
print(s)
"""
Name    Raja
Age       23
"""

data={"Name":"Raja","Age":23, "Mobile":87368732}
s=pd.Series(data, index=["I","II","III","IV"])
print(s)
"""
I      NaN
II     NaN
III    NaN
IV     NaN
"""

data=[10,20,50,40,30]
s=pd.Series(data)
print(s[2]) #50 

data=[10,20,50,40,30]
s=pd.Series(data, index=[0,1,2,3,4])
print(s[[1,2,3]])
"""
1    20
2    50
3    40
"""