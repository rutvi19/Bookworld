from django.db import models
from userapp.models import *

# Create your models here.
class add_book_cls(models.Model): 
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    image = models.ImageField()

class order(models.Model):
    STATUS_CHOICES = (
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(regisdata, on_delete=models.CASCADE)    
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    total_price = models.FloatField(default=0.0) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"