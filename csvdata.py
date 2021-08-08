import pandas as pd 
df=pd.read_csv("data.csv", squeeze=True) 
#print(df)

#max=df["marksC"].max()
#print(max)

#date=df["Date"]
#print(date)

#head=df.head(3)
#print(head)

#columns=df.columns 
#print(columns)

#sort=df.sort_values(["marksC"], ascending=[False])
#print(sort)

#sum=df["marksA"]+df["marksB"]+df["marksC"]
#print(sum)

#df=df.drop(columns=["Total"])
#print(df)

#loc=df.iloc[1:4] #row wise
#print(loc)

#loc=df.iloc[:, 1:4] #col-wise
#print(loc)

#marksA=df.iloc[:, 3:4]#3rd column
#print(marksA)

#loc=df.loc[(df["marksC"]==87)]
#print(loc)

#loc=df.loc[(df["marksA"]==56) & (df["marksC"]==87)]
#print(loc)

df['count'] = 1
group=df.groupby(['marksA', 'marksC']).count()['count']
print(group)







