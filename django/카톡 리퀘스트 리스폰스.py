#Views.py




from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytoon.settings")
import django
django.setup()

from pytoon.models import User


# Create your views here.

def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['초기 설정', '추가', '삭제']
    })
@csrf_exempt


def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']
    userid= received_json_data['user_key']

    if content=='초기 설정':

        create_user_db(request)
        
        return JsonResponse({
                'message': {
                    'text': '초기 설정 되었습니다' + get_user_db(request)
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['초기 설정', '목록', '추가/삭제']
                }

            })
    elif content=='목록':
        return JsonResponse({
                'message': {
                    'text': '현재 당신의 웹툰 목록입니다.'+get_user_db(request) # 유저 db목록
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['초기 설정', '목록', '추가/삭제']
                }

            })
    elif content=='추가/삭제':
        return JsonResponse({
                'message': {
                    'text': content + '할 웹툰을 입력해주세요'  # 유저 db목록
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['초기 설정', '목록', '추가/삭제']
                }

            })
    else: # 만화이름으로 입력이 들어올 경우
        append_delete_db(request)
        return JsonResponse({
                'message': {
                    'text': '당신의 웹툰목록입니다.'+ get_user_db(request)  # 유저 db목록
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['초기 설정', '목록', '추가/삭제']
                }
        

        
# 왜 오류가 뜰까?    
def create_user_db(request):  
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']
    userid= received_json_data['user_key']
                
    content=[content] # 추후 삽입, 삭제를 위해 리스트로 만듬
     
    Menu.objects.create(
        user_id=user_id,
        user_toon=content,
        
        )
        
                
def get_user_db(request):
        json_str = ((request.body).decode('utf-8'))
        received_json_data = json.loads(json_str)
        userid= received_json_data['user_key']
                
        toon_name = User.objects.get(user_id=userid).toon_name

        return '당신의 웹툰 목록입니다' + toon_name


def append_delete_db(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']

    a=User.objects.get(user_id=userid).user_toon



#Models.py

from django.db import models

# Create your models here.
#유저별 DB
class User(models.Model):
   user_id = models.CharField(max_length=30, default="")
   user_toon= models.CharField(max_length=30, default="")
   
   def __str__(self):
      return self.user_id


    if content in a:
        a.remove(content)
    else:
        a.append(content)


