from django.conf.urls import url
from django.contrib import admin
from .views import post_model , login , post_model_detail , post_model_create , post_model_delete

urlpatterns = [

        url(r'^create/$', post_model_create, name='create'),
        url(r'^$', post_model, name="post_model"),
        url(r'^login/', login, name='login'),
        url(r'^(?P<id>\d+)/$', post_model_detail, name='detail'),
        url(r'^(?P<id>\d+)/delete/$', post_model_delete, name='delete'),


]
