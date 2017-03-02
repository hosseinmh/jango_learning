from django.conf.urls import url
from django.contrib import admin
from .views import post_model

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url (r'^$',home , name="home"),
    # url(r'^redirect/',redirect, name="redirect"),
         url(r'^$',post_model , name="post_model"),
]
