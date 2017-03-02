from django.shortcuts import render
from .models import PostModel
from django.http import HttpResponse
# Create your views here.

def post_model(request):
    qs = PostModel.objects.all()
    #  print(qs)
    # return HttpResponse("some new data")
    template  = "web/index_list.html"
    context ={
         "objext_list":qs
    }
    return render(request ,template ,context)
