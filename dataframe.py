#1
import pandas as pd 
data=[1,2,3,4,5]
df=pd.DataFrame(data)
#print(df)


#Add Columns
data=[["Raja",23],["Anbu",22],["Siva",25]]
df=pd.DataFrame(data,columns=["Name","Age"])
#print(df)

#Change the data type
data=[["Raja",23],["Anbu",22],["Siva",25]]
df=pd.DataFrame(data,columns=["Name","Age"], dtype=float)
#print(df)

#Dict of ndarrays
data={"Name":["Raja","Anbu","Siva"], "Age":[23,22,25]}
df=pd.DataFrame(data)
#print(df)

#indexed DataFrame
data={"Name":["Raja","Anbu","Siva"], 
       "Age":[23,22,25]}
df=pd.DataFrame(data, index=["I","II","III"])
#print(df)




#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data)
#print(df)

"""
NaN, standing for not a number, is a member of a numeric data type that can be interpreted as 
a value that is undefined or unrepresentable, especially in floating-point arithmetic.
"""
#List of Dictionaries
data=[{"Name":"Anbu","Age":22,"Mobile":7623873},
      {"Name":"Raja","Age":23,},
      {"Name":"Siva","Age":24,"Mobile":9878967}
      ]
df=pd.DataFrame(data, index=["Rank1","Rank2","Rank3"] , 
   columns=["Name","Age","Mobile Number"] )
#print(df)

data={
      "Name":pd.Series(["Arun","Kanna","Kesav"],  
                index=[1,2,3]),
      "Age":pd.Series([22,24,23],  
                index=[1,2,4])
}
df=pd.DataFrame(data)
#print(df)
#print(df["Name"])

""" Add a new column """
df["Mobile"]=pd.Series([627732,732737,547547],
             index=[1,2,3])
print(df)

""" delete column """
del df["Mobile"]
print(df)

