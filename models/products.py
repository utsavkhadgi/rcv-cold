from django.db import models

# Create your models here.
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=False)
    price = models.FloatField(null=False)
    description = models.TextField(max_length=200,null=False)

    class Meta:
        app_label  = 'products'

    def __str__(self):
        return self.title

    
