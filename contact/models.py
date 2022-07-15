from cProfile import label
from dataclasses import field
from pickle import TRUE
from django.db import models

from django import forms

role_choice=[
    ('0', "Regular - Can't delete members"),
    ('1', "Admin - Can delete members")
]

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=500, null=True)
    last_name = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    role = models.CharField( max_length=10, choices = role_choice, blank=False, default=None)

    def __str__(self):
        return self.first_name
