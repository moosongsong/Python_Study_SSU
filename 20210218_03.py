from numpy import NAN, nan, NaN

# 데이터 자체가 없음을 의미한다.
# 따라서 비교자체를 할 수가 없다.
print(nan == nan)
print(NAN == NAN)
print(NaN == NaN)

import pandas as pd
import numpy as np

ebola = pd.read_csv("country_timeseries.csv")
print(ebola.count())  # 값이 존재하는 항목의 개수를 출력한다.

print(np.count_nonzero(ebola.isnull()))  # 값이 존재하지 않는 항목의 개수를 출력한다.

ebola.fillna(0)  # Nan 값을 0으로 채워라.

ebola.fillna(method='ffill')  # 값이 없는 경우 앞에 있는 값을 가져다가 쓴다.
ebola.fillna(method='bfill')  # 값이 없는 경우 뒤에 있는 값을 가져다가 쓴다.
ebola.interpolate()  # 값이 없는 경우 앞과 뒤에 있는 값의 평균값을 쓴다.
ebola.dropna()  # 값이 하나라도 없는 경우 그 행 자체를 날려버린다.

# melt 사용해보기
ebola2 = pd.melt(ebola, id_vars=['Date', 'Day'])
print(ebola2)

ebola_split = ebola2['variable'].str.split('_')
print(ebola_split)

status = ebola_split.str.get(0)
print(status)

country = ebola_split.str.get(1)
print(country)

ebola2['status'] = status
ebola2['country'] = country
print(ebola2)

ebola2 = ebola2[['Date', 'Day', 'status', 'country', 'value']]
print(ebola2)