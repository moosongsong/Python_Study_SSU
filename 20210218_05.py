import pandas as pd

weather = pd.read_csv("weather.csv")
# del weather['id']
# del weather['year']
print(weather)

result = pd.melt(weather, id_vars=['id', 'year', 'month', 'element'], var_name='day', value_name='temp')
print(result)

result2 = result.pivot_table(index=['id', 'year', 'month', 'day'], columns='element', values='temp', dropna=False)
print(result2)

result2 = result2.reset_index()
print(result2)