from django.conf.urls import url
from django.contrib import admin
from .views import post_model , login , post_model_detail , post_model_create

urlpatterns = [

        url(r'^$', post_model, name="post_model"),
        url(r'^login/', login, name='login'),
        url(r'^(?P<id>\d+)/$', post_model_detail, name='detail'),
        url(r'^create/$', post_model_create, name='create')

]
