# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Tweet(models.Model):
    user=models.TextField()
    text=models.TextField()
    links=models.TextField()
    domain=models.TextField()
