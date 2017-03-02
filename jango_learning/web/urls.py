from django.conf.urls import url
from django.contrib import admin
from .views import post_model , login , post_model_detail

urlpatterns = [
#url(r'^admin/', admin.site.urls),
# url (r'^$',home , name="home"),
# url(r'^redirect/',redirect, name="redirect"),
        url(r'^$', post_model, name="post_model"),
        url(r'^login/', login, name='login'),
        url(r'^1/$', post_model_detail, name='detail')

]
