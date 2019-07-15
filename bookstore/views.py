from django.shortcuts import render


# Create your views here.
def firstdefination(request):
    return render(request, "FirstHtml.html")
