# Generated by Django 4.2.4 on 2023-08-29 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0004_alter_calendar_current_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 29, 13, 20, 14, 186452)),
        ),
    ]
