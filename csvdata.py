import pandas as pd 
df=pd.read_csv("data.csv") 

print("Entire CSV File")
print(df)

print("Maximum: ")
max=df["marksC"].max()
print(max)

print("Particular Column: ")
date=df["Date"]
print(date)

print("1st 3 Rows")
head=df.head(3)
print(head)

print("Only Column Names: ")
columns=df.columns 
print(columns)

print("Sort Columns Values: ")
sort=df.sort_values(["marksC"], ascending=[False])
print(sort)

print("Sum of columns values: ")
sum=df["marksA"]+df["marksB"]+df["marksC"]
print(sum)

print("Drop particular columns: ")
df=df.drop(columns=["Total"])
print(df)

print("Row Wise: ")
loc=df.iloc[1:4] #row wise => row 1,2,3 (index,1,2,3)
print(loc)

print("Columns Wise: ")
loc=df.iloc[:, 1:4] #col-wise => col 1,2,3
print(loc)

print("3rd Columns: ")
marksA=df.iloc[:, 3:4]#3rd column
print(marksA)

print("Filter row: ")
loc=df.loc[(df["marksC"]==87)]
print(loc)

loc=df.loc[(df["marksA"]==56) & (df["marksC"]==87)]
print(loc)

print("Count: ")
df['count'] = 1
group=df.groupby(['marksA', 'marksC']).count()['count']
print(group)


"""
Entire CSV File
       Date   name  age  marksA  marksB  marksC  Total
0  01-01-19  Guhan   23      67      78      54    222
1  02-01-19   Anbu   25      56      45      87    193
2  03-01-19   Raja   22      45      73      94    234
3  04-01-19  Kamal   21      56      67      87    231
4  05-01-19   Siva   24      63      74      84    245
Maximum:
94
Particular Column:
0    01-01-19
1    02-01-19
2    03-01-19
3    04-01-19
4    05-01-19
Name: Date, dtype: object
1st 3 Rows
       Date   name  age  marksA  marksB  marksC  Total
0  01-01-19  Guhan   23      67      78      54    222
1  02-01-19   Anbu   25      56      45      87    193
2  03-01-19   Raja   22      45      73      94    234
Only Column Names:
Index(['Date', 'name', 'age', 'marksA', 'marksB', 'marksC', 'Total'], dtype='object')
Sort Columns Values:
       Date   name  age  marksA  marksB  marksC  Total
2  03-01-19   Raja   22      45      73      94    234
1  02-01-19   Anbu   25      56      45      87    193
3  04-01-19  Kamal   21      56      67      87    231
4  05-01-19   Siva   24      63      74      84    245
0  01-01-19  Guhan   23      67      78      54    222
Sum of columns values:
0    199
1    188
2    212
3    210
4    221
dtype: int64
Drop particular columns:
       Date   name  age  marksA  marksB  marksC
0  01-01-19  Guhan   23      67      78      54
1  02-01-19   Anbu   25      56      45      87
2  03-01-19   Raja   22      45      73      94
3  04-01-19  Kamal   21      56      67      87
4  05-01-19   Siva   24      63      74      84
Row Wise:
       Date   name  age  marksA  marksB  marksC
1  02-01-19   Anbu   25      56      45      87
2  03-01-19   Raja   22      45      73      94
3  04-01-19  Kamal   21      56      67      87
Columns Wise:
    name  age  marksA
0  Guhan   23      67
1   Anbu   25      56
2   Raja   22      45
3  Kamal   21      56
4   Siva   24      63
3rd Columns:
   marksA
0      67
1      56
2      45
3      56
4      63
Filter row:
       Date   name  age  marksA  marksB  marksC
1  02-01-19   Anbu   25      56      45      87
3  04-01-19  Kamal   21      56      67      87
       Date   name  age  marksA  marksB  marksC
1  02-01-19   Anbu   25      56      45      87
3  04-01-19  Kamal   21      56      67      87
Count: 
marksA  marksC
45      94        1
56      87        2
63      84        1
67      54        1
Name: count, dtype: int64
"""






