from django.db import models


# Create your models here.
class regisdata(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True,null=True)

class cart(models.Model):
    user_id = models.IntegerField()  # Session user id store કરવા
    product = models.ForeignKey('adminapp.add_book_cls', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def total_cost(self):
        return self.quantity * self.product.price
    
class checkout(models.Model):
    user = models.ForeignKey('regisdata', on_delete=models.CASCADE) 
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True) 
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    total_price = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fname
    
class contact_cls(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

class notes_cls(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='MyNotes')
    description = models.CharField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)