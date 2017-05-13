from django.conf.urls import url, include

from rest_framework import routers

from . import views

urlpatterns = [
    url(r'^api/search/(?P<author>[\w]+)/exact/$', views.exact),
    url(r'^api/search/(?P<author>[\w]+)/partial/$', views.partial),
    url(r'^api/populate/$', views.populate),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
