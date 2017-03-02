from django.shortcuts import render
from .models import PostModel
from django.http import HttpResponse
# Create your views here.

def post_model(request):
    qs = PostModel.objects.all()
    print(request.user)
    if request.user.is_authenticated():
        print ("logged in ")
    else :
        print ("not logged in ")


    # return HttpResponse("some new data")
    template = "web/index_list.html"
    context = {
         "object_list": qs
    }
    return render(request, template, context)
