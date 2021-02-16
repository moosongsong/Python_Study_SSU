#연금복권 전회차 로또번호 긁어오고 엑셀로 저장하기

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%97%B0%EA%B8%88%EB%B3%B5%EA%B6%8C").text
html = BeautifulSoup(url, "html.parser")

current = int(html.find('a', attrs={'class': '_lottery-btn-current'}).find('em').text[:-1])
print(current)

total = []
for i in range(1, current + 1):
    url = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%97%B0%EA%B8%88%EB%B3%B5%EA%B6%8C+{}%ED%9A%8C".format(
            i)).text
    html = BeautifulSoup(url, "html.parser")
    numbers = html.find('ul', attrs={'class': 'win_num'}).find_all('span')
    box = []
    for n in numbers:
        box.append(int(n.text[0]))
    box.append(i)
    total.append(box)

y_lotto = pd.DataFrame({
    '회차': [i[7] for i in total],
    '금액': [i[0] for i in total],
    '1번째':[i[1] for i in total],
    '2번째':[i[2] for i in total],
    '3번째':[i[3] for i in total],
    '4번째':[i[4] for i in total],
    '5번째':[i[5] for i in total],
    '6번째':[i[6] for i in total]
})

y_lotto.to_excel('y_lotto.xlsx', sheet_name='Sheet1')