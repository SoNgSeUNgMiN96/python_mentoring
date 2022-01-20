import requests
import os
from bs4 import BeautifulSoup
import time


title = '독립일기'  #무슨 웹툰이든 아무거나 넣으면 됨.

dirName = 'webtoon'
if not os.path.isdir(dirName):
    os.mkdir(dirName)
os.chdir(dirName)

if not os.path.isdir(title):
    os.mkdir(title)
os.chdir(title)


for episode in range(1,144):
    url = 'https://comic.naver.com/webtoon/detail?titleId=748105&no='+str(episode)+'&weekday=sun'
    response = requests.get(url)


    req_header = {
        'referer': url
    }

    if response.status_code == 200:     #에러가 없었을 때

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        tag = '#comic_view_area > div.wt_viewer > img'
        imgs = soup.select(tag)

        # 디렉토리 생성
        dirName = title+' '+str(episode)+'화'
        if not os.path.isdir(dirName):
            os.mkdir(dirName)

        for idx,img in enumerate(imgs,1):

            fileName = os.getcwd()+'/'+dirName+'/'+title+' '+str(episode)+'화'+repr(idx)+'.jpg'
            print(fileName)
            with open(fileName,"wb") as file:
                src = requests.get(img.get("src"),headers=req_header)
                file.write(src.content)
            time.sleep(0.5)
    else :
        print(response.status_code)

