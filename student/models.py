from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=20)