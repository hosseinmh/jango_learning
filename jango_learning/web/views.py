from django.shortcuts import render
from .models import PostModel
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
#@login_required(login_url='web/login/')# in future use this to load login page

def post_model(request):

    qs = PostModel.objects.all()
    print(request.user)

    context = {
        "object_list": qs
    }

    if request.user.is_authenticated():
        template = "web/index_list.html"
        print ("logged in ")
    else:
        template = "web/404.html"
        return HttpResponseRedirect("/web/login/")
        print ("not logged in ")

    return render(request, template, context)

def login(request):

    template = "web/login.html"
    context = {

    }
    return render(request, template, context)