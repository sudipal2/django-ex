from django.shortcuts import render
from django.http import HttpResponse

from .objectStorage import get_item

def index(request):
    return HttpResponse("This a is microservice to pull images from ibm cloud storage.")

def fetchimage(request, item_id):
    bucket_name = "gamification-cos-standard-tkq"
    try:
        f = item_id + '.jpg'
        img_data = get_item(bucket_name=bucket_name, item_name=f)
        if img_data:
            return HttpResponse(img_data, content_type="image/jpg")
        else:
            return HttpResponse('image not found')
            
    except Exception as e:
        return HttpResponse(e)
