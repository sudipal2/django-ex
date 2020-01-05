from django.shortcuts import render
from django.http import HttpResponse

from .objectStorage import get_item, get_all_items

def index(request):
    return HttpResponse("This a is microservice to pull images from ibm cloud storage.")

def fetchimage(request, item_id):
    bucket_name = "gamification-cos-standard-tkq"
    try:
        f = item_id + '.jpg'
	#print('Trying to find ',f)
        img_data = get_item(bucket_name=bucket_name, item_name=f)
        if img_data:
            return HttpResponse(img_data, content_type="image/jpg")
        else:
            return HttpResponse('image not found')
            
    except Exception as e:
        return HttpResponse(e)

def fetchallimages(request):
    bucket_name = "gamification-cos-standard-tkq"
    try:
	#print('Trying to find ALL images')
        i = 1
        img_ct = 1000
        while i < 6:
	    i += 1
	    img_ct += 1
            #img_data = get_all_items(bucket_name=bucket_name)
	    img_data = get_item(bucket_name=bucket_name, img_ct)
            if img_data:
                return HttpResponse(img_data, content_type="image/jpg")
            else:
                return HttpResponse('image not found')
            
    except Exception as e:
        return HttpResponse(e)
