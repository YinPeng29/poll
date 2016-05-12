from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^$','pollapp.views.index',name='index'),
    url(r'^(?P<question_id>[0-9]+)/$','pollapp.views.detail',name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$','pollapp.views.results',name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$','pollapp.views.vote',name='vote'),
]