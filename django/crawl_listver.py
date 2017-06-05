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



#초기화 함수(처음에만 사용)
def initialization():
    url = "http://comic.naver.com/webtoon/period.nhn#"
    data = urlopen(url)
    source = data.read()
    data.close()
    soup = BeautifulSoup(source,"lxml")
    webtoons = soup.find_all("div","thumb")
    #웹툰명을 저장
    names = [div.a['title'] for div in webtoons]
    #웹툰 최신화 리스트 페이지
    links = [div.a["href"] for div in webtoons]
    for i in range(len(links)):
        links[i] = ("http://comic.naver.com"+links[i]) 
    first = []
    changed=[0 for i in range(len(links))]
    for i in range(len(links)):
        wlist = urlopen(links[i])
        wsource = wlist.read()
        wlist.close()
        wsoup = BeautifulSoup(wsource,'lxml')
        wweb = wsoup.find_all("td","title")
        wn = "http://comic.naver.com"+wweb[0].a["href"]
        first.append(wn)
    
    return [names,links,first,changed]


def syncro(alist):
#동기화
    
    for i in range(len(alist[0])):
        wlist = urlopen(alist[1][i])
        wsource = wlist.read()
        wlist.close()
        wsoup = BeautifulSoup(wsource,'lxml')
        wweb = wsoup.find_all("td","title")
        wn = "http://comic.naver.com"+wweb[0].a["href"]
        if wn != alist[2][i]:
            alist[2][i] = wn
            alist[3][i] = 1
        else:
            alist[3][i] = 0
        return alist
            #1/0을 굳이 만들지 않아도 전송하는 방식을 만들 필요 있음.
   #이렇게 값이 1로 바뀌면 전송 필요
#시간마다 자동으로 돌아가게 하는 코드 필요.
#15분 간격으로 반복문을 돌릴 것을 고려하여 작성.

if __name__=='__main__':
    A = initialization()
    A = syncro(A)
    for i in range(len(A[1])):
        Webtoon(Name = A[0][i], List = A[1][i], New = A[2][i], Changed = A[3][i]).save()




        
