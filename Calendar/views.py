from django.shortcuts import render
from .models import Calendar
from django.http import HttpResponse


def date(request):
    dates = Calendar.objects.all()
    output = ", ".join([str(date.current_date) for date in dates])
    return HttpResponse(output[-10:])


