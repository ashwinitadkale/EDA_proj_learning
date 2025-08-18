import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,26,27],
    'City':['Delhi','Mumbai','Chennai']
}
df=pd.DataFrame(data)
print(df)
series=pd.Series([10,12,13],name="Numbers")
print(series)