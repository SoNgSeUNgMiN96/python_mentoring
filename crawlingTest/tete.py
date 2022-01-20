import requests
from bs4 import BeautifulSoup
import os

main_url = 'https://comic.naver.com/webtoon/detail?titleId=727188&no=143&weekday=sat'
res = requests.get(main_url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')

img_urls = []
for img_url in soup.select("#comic_view_area > div.wt_viewer > img"):
    img_urls.append(img_url['src'])

# 디렉토리 생성
if not os.path.isdir('img'):
    os.mkdir('img')

for real_url in img_urls:
    req_header = {
        'referer': main_url
    }

    res2 = requests.get(real_url, headers=req_header)
    print(res2)
    img_data = res2.content
    file_name = os.path.basename(real_url)
    print(file_name)
    with open('img/' + file_name, 'wb') as file:
        print('Writing to {} ({} bytes)'.format(file_name, len(img_data)))
        file.write(img_data)