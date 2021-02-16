#코스피 코스닥 종합정보 가지고 오기

from bs4 import BeautifulSoup
import requests
import pandas as pd
from tqdm import tqdm #for문의 진행사항을 알수 있는 라이브러리

# pip install lxml

#코스피 해보기
url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?&page=1").text
html = BeautifulSoup(url, "html.parser")

kospi_page = html.find('td', attrs={'class': 'pgRR'}).find('a')['href']
kospi_page = int(kospi_page.split('&')[-1].split('=')[-1])

kospi_box = []
for n in tqdm(range(1, kospi_page+1)):
    url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(n)).text
    html = BeautifulSoup(url, "html.parser")

    table = html.find('table', attrs={'class': 'type_2'})
    table = pd.read_html(str(table))[0]
    table = table[table['종목명'].notnull()]
    del table['토론실']
    table['종류'] = ['KOSPI']*len(table)
    kospi_box.append(table)

kospi= pd.concat(kospi_box, ignore_index=True)

#코스닥 해보기
url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page=1").text
html = BeautifulSoup(url, "html.parser")

kosdaq_page = html.find('td', attrs={'class': 'pgRR'}).find('a')['href']
kosdaq_page = int(kosdaq_page.split('&')[-1].split('=')[-1])

kosdaq_box = []
for n in tqdm(range(1, kosdaq_page+1)):
    url = requests.get("https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page={}".format(n)).text
    html = BeautifulSoup(url, "html.parser")

    table = html.find('table', attrs={'class': 'type_2'})
    table = pd.read_html(str(table))[0]
    table = table[table['종목명'].notnull()]
    del table['토론실']
    table['종류'] = ['KOSDAQ']*len(table)
    kosdaq_box.append(table)

kosdaq = pd.concat(kosdaq_box, ignore_index=True)

totalStock = pd.concat([kospi, kosdaq], ignore_index=True)
print(totalStock)