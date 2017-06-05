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

row = Webtoon.objects.get(pk=1)

print(row.Name)
