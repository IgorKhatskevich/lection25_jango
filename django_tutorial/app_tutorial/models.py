from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    pages_numbers = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.book}, {self.user}'