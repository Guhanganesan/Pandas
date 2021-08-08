# pandas.Series( data, index, dtype, copy)
import pandas as pd 
#print(pd.Series())

s=pd.Series(["Raja","Anbu","Siva"])
#print(s)

s=pd.Series(["Raja","Anbu","Siva"],index=["A","B","C"])
#print(s)

data=[{"Name":"Raja","Age":23},{"Name":"Anbu","Age":22}]
s=pd.Series(data)
#print(s)

data={"Name":"Raja","Age":23}
s=pd.Series(data)
#print(s)

data={"Name":"Raja","Age":23, "Mobile":87368732}
s=pd.Series(data, index=["I","II","III","IV"])
print(s)

data=[10,20,50,40,30]
s=pd.Series(data)
print(s[2])

data=[10,20,50,40,30]
s=pd.Series(data, index=[0,1,2,3,4])
print(s[[1,2,3]])
