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
        'buttons' : ['�ʱ� ����', '�߰�', '����']
    })
@csrf_exempt


def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']
    userid= received_json_data['user_key']

    if content=='�ʱ� ����':

        create_user_db(request)
        
        return JsonResponse({
                'message': {
                    'text': '�ʱ� ���� �Ǿ����ϴ�' + get_user_db(request)
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['�ʱ� ����', '���', '�߰�/����']
                }

            })
    elif content=='���':
        return JsonResponse({
                'message': {
                    'text': '���� ����� ���� ����Դϴ�.'+get_user_db(request) # ���� db���
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['�ʱ� ����', '���', '�߰�/����']
                }

            })
    elif content=='�߰�/����':
        return JsonResponse({
                'message': {
                    'text': content + '�� ������ �Է����ּ���'  # ���� db���
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['�ʱ� ����', '���', '�߰�/����']
                }

            })
    else: # ��ȭ�̸����� �Է��� ���� ���
        append_delete_db(request)
        return JsonResponse({
                'message': {
                    'text': '����� ��������Դϴ�.'+ get_user_db(request)  # ���� db���
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['�ʱ� ����', '���', '�߰�/����']
                }
        

        
# �� ������ ���?    
def create_user_db(request):  
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']
    userid= received_json_data['user_key']
                
    content=[content] # ���� ����, ������ ���� ����Ʈ�� ����
     
    Menu.objects.create(
        user_id=user_id,
        user_toon=content,
        
        )
        
                
def get_user_db(request):
        json_str = ((request.body).decode('utf-8'))
        received_json_data = json.loads(json_str)
        userid= received_json_data['user_key']
                
        toon_name = User.objects.get(user_id=userid).toon_name

        return '����� ���� ����Դϴ�' + toon_name


def append_delete_db(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    content= received_json_data['content']

    a=User.objects.get(user_id=userid).user_toon



#Models.py

from django.db import models

# Create your models here.
#������ DB
class User(models.Model):
   user_id = models.CharField(max_length=30, default="")
   user_toon= models.CharField(max_length=30, default="")
   
   def __str__(self):
      return self.user_id


    if content in a:
        a.remove(content)
    else:
        a.append(content)


