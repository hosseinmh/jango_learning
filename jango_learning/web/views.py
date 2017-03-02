from django.shortcuts import render , get_object_or_404
from .models import PostModel
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect ,Http404





def post_model_detail(request):

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

    qs = PostModel.objects.filter(id=1)
    if not qs.exists():
        raise Http404
    else:
        obj = qs.first()


    template = "web/post_model_detail.html"
    context = {
        "object" :obj
    }
    return render(request, template, context)


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