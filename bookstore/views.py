from django.shortcuts import render


# Create your views here.
def firstdefination(request):
    return render(request, "FirstHtml.html")

def store(request):
    return render(request,"Store.html")


def fiction(request):
    return render(request,"fiction.html")