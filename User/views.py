from django.shortcuts import render
from .models import User
from django.http import HttpResponse


def user_display(request):
    users = User.objects.all()
    name_lastname_age = []
    for user in users:
        name_lastname_age.append(user.first_name + " ")
        name_lastname_age.append(user.last_name+" ")
        age = (user.today_date - user.date_of_birth)/365
        clean_age = ""
        for letter in str(age):
            if letter !=" ":
                clean_age += letter
            else:
                break
        name_lastname_age.append(clean_age + " years, ")
    return HttpResponse(name_lastname_age)
