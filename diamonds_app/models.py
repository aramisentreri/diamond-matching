# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Diamond(models.Model):

    carat = models.DecimalField(max_digits = 4, decimal_places=2)
    clarity = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)
    cut = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

