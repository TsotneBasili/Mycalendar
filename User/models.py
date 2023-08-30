from django.db import models
from datetime import datetime


class User(models.Model):
    first_name = models.CharField(max_length=30, default="name")
    last_name = models.CharField(max_length=50, default="surname")
    date_of_birth = models.DateField(default=datetime.now)
    today_date = models.DateField(default=datetime.now)

