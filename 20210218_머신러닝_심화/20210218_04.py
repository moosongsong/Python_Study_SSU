import pandas as pd

pew = pd.read_csv("pew.csv")
print(pew)

billboard2 = pd.melt(pew, id_vars='religion', var_name='income', value_name='count')
print(billboard2)

billboard = pd.read_csv("billboard.csv")
print(billboard)
billboard2 = pd.melt(billboard, id_vars=['year', 'artist', 'track', 'time', 'date.entered'], var_name='week',
                     value_name= 'rating')
print(billboard2)

#

billboard3 = billboard2[['year', 'artist', 'track', 'time']]
print(billboard3)

result = billboard3[billboard3['track']=='Loser']
result = result.drop_duplicates()
print(result)