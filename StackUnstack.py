from pandas import DataFrame
import pandas as pd
import numpy as np 

"""
df=pd.DataFrame(np.random.rand(4,2), index=[['a','a','b','b'],[1,2,1,2]],
                                columns=['data1','data2'])

print(df)
"""

"""
data={
     ('California',2000):7678678,
     ('California',2010):868688,
     ('Texas',2000):4345355,
     ('Texas',2010):4635476,
     ('New York',2000):5432546,
     ('New York',2010):8767244
}
s=pd.Series(data)

print(s)
"""

"""
x=pd.MultiIndex.from_arrays([['a','a','b','b'],[1,2,1,2]])
print(x)

"""

arrays=[
    ['Week1','Week1','Week2','Week2','Week3','Week3','Week4','Week4'],
    ['1.Python','2.GitHub','3.MatPlotLib','4.SQL','5.PokeMan','6.OPP','7.Pandas','8.Stats']
]

ar2=[
    ['StudentA','StudentA','StudentB','StudentB'],['Labs','Proj','Labs','Proj']
]

data=[[60,70,80,80,60,90,70,80],
      [100,70,70,70,60,80,70,80],
      [50,70,80,80,60,90,70,80],
      [50,70,60,80,68,70,60,70]
      ]

data=np.array(data)
df=pd.DataFrame(data, index=ar2, columns=arrays)

#print(df)

df1=df.unstack()

#print(df1)

df_orig=df1.stack()
#print(df_orig)

df2=df1.unstack()
print(df2)










