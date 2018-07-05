from django.db import models
from django.contrib.auth.models import *
# Create your models here.
from django.db import models
import datetime
from django.contrib.auth.models import *
# Create your models here.

class Card(models.Model):
    friendly_name = models.CharField(max_length=32)
    name_on_card = models.CharField(max_length=128)
    expiry_date=models.DateField(null=True,blank=True)
    typec = models.CharField(max_length=64)
    cvv=models.CharField(max_length=3)
    card_number=models.CharField(max_length=20)

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name_on_card


