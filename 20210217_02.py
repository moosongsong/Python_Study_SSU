# 읽어온 데이터 조작하기

import pandas as pd  # 데이터 분석 툴

# 데이터 읽어와서 저장하기
scientist = pd.read_csv('scientists.csv')
print(scientist)
print(scientist.info())

# 나이만 추출하기
ages = scientist['Age']
print(ages)
print(ages.max())  # 최대
print(ages.min())  # 최소
print(ages.mean())  # 평균

# 평균나이보다 많은 나이 출력하기
print(ages > ages.mean())  # bool 값 반환
print(ages[ages > ages.mean()])  # 맞는 값 출력

print(scientist[scientist['Age'] > scientist['Age'].mean()])

print(ages * ages)
print(ages * 2)

a = pd.Series([100, 100])

print(ages + a)

# 문자열을 날짜로 취급하기
born = pd.to_datetime(scientist['Born'], format='%Y-%m-%d')
died = pd.to_datetime(scientist['Died'], format='%Y-%m-%d')
print(born)
print(died)

# 새로운 열 추가하기
scientist['born_dt'] = born
scientist['died_dt'] = died
print(scientist)
print(scientist.info())

# 원하는 데이터만 추려서 만들기
scientist = scientist[['Name', 'born_dt', 'died_dt', 'Age', 'Occupation']]
print(scientist)

# datetime 계산 결과로 새로운 열 만들기
scientist['days'] = scientist['died_dt'] - scientist['born_dt']
print(scientist)
