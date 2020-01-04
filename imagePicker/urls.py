from django.conf.urls import include, url

from . import views
print "Step 1 from url.py"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^get-image-for-item-id/(?P<item_id>[0-9]+)/$', views.fetchimage, name='fetchimage'),
    url(r'^get-all-image/$', views.fetchallimages, name='fetchallimages')
]