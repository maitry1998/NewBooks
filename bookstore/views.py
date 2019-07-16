from django.shortcuts import render
from .models import Book

# Create your views here.
def firstdefination(request):
    return render(request, "FirstHtml.html")

def store(request):
    count= Book.objects.all().count()
    context = {
      "count" : count,
    }
    return render(request,"Store.html",context)


def fiction(request):
    return render(request,"fiction.html")


