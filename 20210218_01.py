import pandas as pd

df1 = pd.read_csv("concat_1.csv")
df2 = pd.read_csv("concat_2.csv")
df3 = pd.read_csv("concat_3.csv")

print(df1)
print(df2)
print(df3)

df4 = pd.concat([df1, df2, df3], ignore_index=True)
print(df4)

df4 = pd.concat([df1, df2, df3], axis=1)
print(df4)

df4 = pd.concat([df1, df2, df3], axis=1, ignore_index=True)
print(df4)

b = pd.Series([100, 100])
print(b)

total = pd.concat([df4, b])
print(total)

# 열이름 바꾸기
df2.columns = ['E', 'F', 'G', 'H']
print(df2)

# 행이름 바꾸기
df2.index = [4,5,6,7]
print(df2)