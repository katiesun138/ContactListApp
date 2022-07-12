from pickle import TRUE
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    # reg = models.CharField(max_length=30)
    # adm = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name
