#네이버 코스피 페이지에 있는 기업이랑 기업 아이디 가지고 오기

from bs4 import BeautifulSoup
import requests
from tqdm import tqdm

url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?&page=1").text
html = BeautifulSoup(url, "html.parser")

kospi_page = html.find('td', attrs={'class': 'pgRR'}).find('a')['href']
kospi_page = int(kospi_page.split('&')[-1].split('=')[-1])

box = []
for n in tqdm(range(1, kospi_page+1)):
    url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(n)).text
    html = BeautifulSoup(url, "html.parser")

    table = html.find('table', attrs={'class': 'type_2'})
    rows = table.find_all('a', attrs={'class': 'tltle'})

    for i in rows:
        test = []
        test.append(i.text)
        test.append(i['href'].split('?')[-1].split('=')[-1])
        box.append(test)

print(box)