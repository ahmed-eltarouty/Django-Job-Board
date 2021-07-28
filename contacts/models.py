from django.db import models
from django.forms.fields import EmailField

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20,blank=True, null=True)
    message = models.TextField()


    def __str__(self):
        return self.name
