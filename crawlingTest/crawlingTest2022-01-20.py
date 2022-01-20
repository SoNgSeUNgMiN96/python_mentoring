import requests
from bs4 import BeautifulSoup

url = 'https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    for i in range(1,11):
        tag = '#s_content > div.section > ul > li:nth-child('+repr(i)+') > dl > dt > a'
        Title = soup.select_one(tag)
        print('지식인 '+repr(i)+'번째 제목 : '+Title.text)



else :
    print(response.status_code)

