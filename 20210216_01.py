#로또 전회차 번호 긁어와서 엑셀로 저장하기

from bs4 import BeautifulSoup  # html을 다루는 라이브러리
import requests  # 요청하다
import pandas as pd  # 데이터분석 툴

url = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90").text
html = BeautifulSoup(url, "html.parser")

# current = html.find('a', attrs={'class': '_lotto-btn-current'}).find('em').text.replace('회', '')
current = int(html.find('a', attrs={'class': '_lotto-btn-current'}).find('em').text[:-1])
print("회차 : " + str(current))

numbers = html.find('div', attrs={'class': 'num_box'}).find_all('span', attrs={'class': 'num'})

box = []
for i in numbers:
    box.append(int(i.text))

print(box)
total = []

for n in range(1, 11):
    url = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90+{}%ED%9A%8C".format(
            n)).text
    html = BeautifulSoup(url, "html.parser")

    numbers = html.find('div', attrs={'class': 'num_box'}).find_all('span', attrs={'class': 'num'})
    box = []
    for i in numbers:
        box.append(int(i.text))

    total.append(box)
    print('{}회 로또 데이터 저장 완료 : {}'.format(n, box))

print(len(total))



#열 : 시리즈
#표 : 데이터프레임
print(
pd.DataFrame({
    '이름' : ['kim', 'min', 'jung'],
    '나이' : [30, 29, 28],
    '성별' : ['남자', '남자', '남자']
}))

lotto = pd.DataFrame({
    '1번': [i[0] for i in total],
    '2번': [i[1] for i in total],
    '3번': [i[2] for i in total],
    '4번': [i[3] for i in total],
    '5번': [i[4] for i in total],
    '6번': [i[5] for i in total],
    '추가': [i[6] for i in total],
})
print(lotto)

lotto.to_excel('lotto.xlsx', sheet_name='Sheet1')

