from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, "FirstHtml.html")

def store(request):
    count= Book.objects.all().count()
    context = {
      "count" : count,
        "page": "welcome to the mystrey books"
    }
    request.session['location'] ="unknown"
    if request.user.is_authenticated:
        request.session['location'] = "unknown"
    return render(request,"base.html",context)


def fiction(request):
    return render(request,"/fiction.html")




