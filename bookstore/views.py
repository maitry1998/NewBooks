from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, "FirstHtml.html")

def store(request):
    books= Book.objects.all()
    context = {
      # "count" : count,
      #   "page": "welcome to the mystrey books"
        'books': books,
    }
    # request.session['location'] ="unknown"
    # if request.user.is_authenticated:
    #     request.session['location'] = "unknown"
    return render(request,"base.html",context)


def fiction(request):
    return render(request,"fiction.html")



def book_detail(request, book_id):

  #  book = get_object_or_404(Book, id=book_id)

    context = {

        'book': Book.objects.get(pk=book_id),

    }
    return render(request,'store/detail.html',context)

