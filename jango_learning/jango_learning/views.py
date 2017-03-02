from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return HttpResponse("<h1> welcome to Django</h1>")
def redirect(request):

    redirect = HttpResponseRedirect("/google/sad")

    return redirect
