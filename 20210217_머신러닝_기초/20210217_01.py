# CSV, TSV 파일 읽어와서 데이터 분석하기


import pandas as pd #데이터 분석 툴
# csv vs tsv : 콤마기준, 탭 기준

df = pd.read_csv('concat_1.csv')
# df = pd.read_csv('concat_1.csv', sep=',')
print(df)

df = pd.read_csv('gapminder.tsv', sep='\t')
print(df)

print(df.head())
print(df.tail())

print(df.shape)
print(df.columns)

print(df.dtypes)

print(df.info())

print(df[['country', 'continent', 'year']])

print(df.loc[0]) #이름으로 접근
print(df.iloc[0]) #위치로 접근

print(df.loc[[0, 10, 1000]])
print(df.iloc[[0, 10, 1000]])
# print(df.loc[-1]) #얘는 에러남
print(df.iloc[-1])

print(df.loc[[0, 10, 1000], ['country', 'year']])
print(df.iloc[[0, 10, 1000], [0,2]])

print(df.iloc[:, [0,2]]) #:은 모든 걸을 의미한다.

a = df.groupby('year')['lifeExp'].mean()
print(a)

# a.to_excel('result.xlsx')

a = df.groupby(['year', 'continent'])['lifeExp'].mean()
print(a)


a= df.groupby('continent')['country'].nunique()
print(a)


pd.Series([100, 100])