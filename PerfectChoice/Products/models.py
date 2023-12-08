from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/')
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
