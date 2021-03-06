from email import message
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=12)
    message = models.TextField()

    def __str__(self):
        return self.name
