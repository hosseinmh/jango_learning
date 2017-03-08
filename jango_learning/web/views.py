from django.shortcuts import render , get_object_or_404
from .models import PostModel
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import PostModelForm
from django.contrib import messages

def post_model_create(request):
    form = PostModelForm( request.POST or None)


    #create a instance from form

    context = {
        "form ": form
    }

    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        messages.success(request , "create a new  web")

    template = "web/create_view.html"

    return render(request, template, context)


def post_model_detail(request , id=None):

    # first way to create a view
    #obj = PostModel.objects.get(id=1)

    # seccond way to create a view
  #  obj = get_object_or_404(PostModel, id=1)

    # thisd way
    # try:
    #     obj =PostModel.get(id=1)
    # except:
    #     raise  Http404

    #fourth way

    qs = PostModel.objects.filter(id=id)
    if not qs.exists():
        raise Http404
    else:
        obj = qs.first()


    template = "web/post_model_detail.html"
    context = {
        "object" :obj
    }
    return render(request, template, context)

def post_model_delete(request , id=None):

    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request,"post deleted")
        return HttpResponseRedirect("/web/")
    context = {
        "object": obj
    }
    template = "web/delete_view.html"
    return render(request , template ,context)



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
