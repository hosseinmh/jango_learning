from django.shortcuts import render
from .models import PostModel
from django.http import HttpResponse


# Create your views here.

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
        print ("not logged in ")

    return render(request, template, context)
