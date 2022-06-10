from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    short = models.CharField(max_length=200 , blank=True)
    image = models.ImageField(upload_to='media' , blank=True)
    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=200)
    short = models.CharField(max_length=200 , blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media' , blank=True)
    color = models.CharField(max_length=200 , blank=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    Name = models.CharField(max_length=300)
    Position = models.CharField(max_length=400)
    Contact = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media' , blank=True)
    about = models.TextField(null=True)

    def __str__(self):
        return f"{self.Name}"
