
## 시간 추가, 자동화.

## 클래스 오브젝트로 이용.

# 10회만 돌아가는

from bs4 import BeautifulSoup
from urllib.request import urlopen
import threading
import datetime

import os

# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'myproject.settings')
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django

django.setup()
from webdata.models import Webtoon

web=[]

# 초기화 함수(처음에만 사용)
def initialization():
    global web
    url = "http://comic.naver.com/webtoon/period.nhn#"
    data = urlopen(url)
    source = data.read()
    data.close()
    soup = BeautifulSoup(source, "lxml")
    webtoons = soup.find_all("div", "thumb")
    # 웹툰명을 저장
    names = [div.a['title'] for div in webtoons]
    # 웹툰 최신화 리스트 페이지
    links = [div.a["href"] for div in webtoons]
    for i in range(len(links)):
        links[i] = ("http://comic.naver.com" + links[i])
    first = []
    changed = [0 for i in range(10)]
    for i in range(len(links)):
        wlist = urlopen(links[i])
        wsource = wlist.read()
        wlist.close()
        wsoup = BeautifulSoup(wsource, 'lxml')
        wweb = wsoup.find_all("td", "title")
        wn = "http://comic.naver.com" + wweb[0].a["href"]
        first.append(wn)
    time = [datetime.datetime.now().strftime('%Y-%m-%d %H:%M') for i in range(10)]
    web= [names, links, first, changed,time]
    for i in range(10):
        Webtoon(Name=names[i], List=links[i], New=first[i], Changed=changed[i], Time=time[i]).save()

def syncro():
    # 동기화
    global web
    while True:
        i=1
        try:
            row = Webtoon.objects.get(pk=i)
            print("부름", end=" ")
            print(row.Name)
        except:
            break
        wlist = urlopen(row.List)
        wsource = wlist.read()
        wlist.close()
        wsoup = BeautifulSoup(wsource, 'lxml')
        wweb = wsoup.find_all("td", "title")
        wn = "http://comic.naver.com" + wweb[0].a["href"]
        if wn != row.New:
            row.New = wn
            row.Changed = 1
            row.Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        else:
            row.Changed = 0
        i+=1

    print("동기화 성공")

    threading.Timer(180, syncro).start()   #3분마다 동작

        # 1/0을 굳이 만들지 않아도 전송하는 방식을 만들 필요 있음.
        # 이렇게 값이 1로 바뀌면 전송 필요

if __name__ == '__main__':
    initialization()
    print("초기화")
    syncro()











