from django.conf.urls import url, include

from rest_framework import routers

from . import views

urlpatterns = [
    url(r'^api/search/(?P<author>.+)/(?P<match>[\w]+)/$', views.search),
    url(r'^api/populate/$', views.populate),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
