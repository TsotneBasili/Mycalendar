from django.db import models
from datetime import datetime


class Calendar(models.Model):
    current_date = models.DateField(default=datetime.now)

