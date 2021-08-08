from collections import OrderedDict
from pandas import DataFrame
import pandas as pd
import numpy as np 

table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item1', 'Item1']),
    ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD',  ['1$', '2$', '3$', '4$']),
    ('EU',   ['1€', '2€', '3€', '4€'])
))
d = DataFrame(table)
#print(d)


p = d.pivot(index='Item', columns='CType', values='USD')

#print(p)

# Original DataFrame: Access the USD cost of Item0 for Gold customers
#print (d[(d.Item=='Item0') & (d.CType=='Gold')].USD.values)

# Pivoted DataFrame: Access the USD cost of Item0 for Gold customers
#print (p[p.index=='Item0'].Gold.values)


p = d.pivot(index='Item', columns='CType')

#print(p)

# Original DataFrame: Access the USD cost of Item0 for Gold customers
#print(d[(d.Item=='Item0') & (d.CType=='Gold')].USD.values)

# Pivoted DataFrame: p.USD gives a "sub-DataFrame" with the USD values only
#print(p.USD[p.USD.index=='Item0'].Gold.values)

p = d.pivot(index='Item', columns='CType')

#print(p)



"""
table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item0', 'Item1']),
    ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD',  ['1',  '2',  '3',  '4']),
    ('EU',   ['1€', '2€', '3€', '4€'])
))
d = DataFrame(table)
p = d.pivot(index='Item', columns='CType', values='USD')
#print(p)  #ValueError: Index contains duplicate entries, cannot reshape

"""

table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item0', 'Item1']),
    ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD',  [1, 2, 3, 4]),
    ('EU',   [1.1, 2.2, 3.3, 4.4])
))
d = DataFrame(table)
p = d.pivot_table(index='Item', columns='CType', values='USD', aggfunc=np.min)
print(p)
