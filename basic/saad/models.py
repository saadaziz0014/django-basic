from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shirt(models.Model):
    SHIRT_TYPES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=1, choices=SHIRT_TYPES)
    picture = models.ImageField("image", upload_to="saad/images", null=True, blank=True)
    
    description = models.TextField(default="")
    
    def __str__(self):
        return self.title
    

class Shop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shop")
    shirt = models.ManyToManyField(Shirt, related_name="shop")
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.location} of {self.user.username}"