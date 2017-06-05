from django.shortcuts import render
from django.http import JsonResponse
import json,datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def keyboard(request):

    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['목록','등록','삭제','추천']
    })
'''
@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('uft-8'))
    received_json_data = json.loads(json_str)
    content = received_json_data['content']

    
    #if content =='등록':
    return JsonResponse({
        'message':{
            'text' : "등록할 웹툰을 정확히 입력하세요."
        }
    })
    
    #if content =='삭제':
        #return JsonResponse({
            #'message':{
             #   'text': "삭제할 웹툰을 정확히 입력하세요."
           # }

        #})
    
'''
