# Generated by Django 4.2.4 on 2023-08-29 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 29, 13, 12, 24, 179820)),
        ),
    ]
