from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s, %s" % (self.last_name,self.first_name)

def cover_upload_path(instance ,filename):
    return '/'.join(['books', str(instance.id) ,filename])

class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    description = models.TextField()
    publishdate=models.DateField(default=timezone.now)
    price=models.DecimalField(decimal_places=2,max_digits=8)
    stock=models.IntegerField(default=0)
    cover_image=models.ImageField(upload_to=cover_upload_path, default='book/empty_cover.jpg')

class Review(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    publish_date=models.DateField(default=timezone.now)
    text=models.TextField()



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)
#this is called from views addtocart fun
    def add_to_carts(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book=book,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except BookOrder.DoesNotExist:
            pass


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()