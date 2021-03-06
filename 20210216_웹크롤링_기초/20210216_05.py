#코로나 관련 뉴스 제목 긁어오기

from bs4 import BeautifulSoup
import requests

total = []
check = 0
news_title = []

for n in range(1, 2000, 10):
    url = requests.get(
        "https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EB%A1%9C%EB%82%98&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=24&start={}&refresh_start=0".format(
            n)).text
    html = BeautifulSoup(url, "html.parser")
    list_news = html.find('ul', attrs={'class': 'list_news'}).find_all('li', attrs={'class': 'bx'})

    for i in list_news:
        title = i.find('a', attrs={'class': 'news_tit'})['title']
        news_title.append(title)
        print(title)

print(news_title)
