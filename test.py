import pandas as pd
data={"Name":"Raja","Age":23, "Mobile":87368732}
s=pd.Series(data, index=["Age","Name","Mobile"])
print(s)
