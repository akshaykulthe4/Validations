import pandas as pd

df = pd.DataFrame(
{
    'Name':['A','B','C','D'],
    'Status':['Father','Mother','Son','Daughter'],
    'DOB':[1966,1969,1994,1995],
    'Age':[56,53,28,27]
}
)

print(df)



result = list(filter(lambda x : x>30 , df['Age']))
print(result)
