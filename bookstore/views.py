from django.shortcuts import render, redirect

from bookstore.forms import ReviewForm
from .models import Book, BookOrder, Cart, Review

from django.core.exceptions import ObjectDoesNotExist

#from django.core.urlresolvers import reverse

from django.utils import timezone

from django.http import JsonResponse

from django.core.mail import EmailMultiAlternatives

from django.template import Context

from django.template.loader import render_to_string

#from django.contrib.gis.geoip import GeoIP

# Create your views here.
def index(request):
    return render(request, "FirstHtml.html")

def store(request):
    book= Book.objects.all()
    context = {
      # "count" : count,
      #   "page": "welcome to the mystrey books"
        'book': book,
    }
    # request.session['location'] ="unknown"
    # if request.user.is_authenticated:
    #     request.session['location'] = "unknown"
    return render(request,"base.html",context)


def fiction(request):
    return render(request,"fiction.html")



def book_detail(request, book_id):
    book=Book.objects.get(pk=book_id)
    context = {
        'book': book,
    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form=ReviewForm(request.POST)
            if form.is_valid():
                new_review = Review.objects.create(
                user=request.user,
                book=context['book'],
                text=form.cleaned_data.get('text')
                )
                new_review.save()
        else:
            if Review.objects.filter(user=request.user , book = context['book']).count() == 0:
                form=ReviewForm()
                context['form'] = form
    context['reviews']=book.review_set.all()

    return render(request,'store/detail.html',context)

def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            cart.add_to_carts(book_id)
        return redirect('cart')
    else:
        return redirect('index')

def remove_from_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')

def cart(request):
    if request.user.is_authenticated:
        cart1 = Cart.objects.get(user=request.user, active=True)
        orders = BookOrder.objects.filter(cart=cart1)
        total = 0
        count = 0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')

#
# def cart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user.id, active=True)
#         orders = BookOrder.objects.filter(cart=cart)
#         total = 0
#         count = 0
#         for order in orders:
#             total += (order.book.price * order.quantity)
#             count += order.quantity
#         context = {
#             'cart': orders,
#             'total': total,
#             'count': count,
#         }
#         return render(request, 'store/cart.html', context)
#     else:
#         return redirect('index')


