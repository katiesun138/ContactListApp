from cProfile import label
from pickle import TRUE
from django.db import models

role_choices=[
    ('admin', 'Admin'),
    ('regular', 'Regular')
]

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    adm = models.CharField(max_length=20, null=True)
    reg = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.first_name
