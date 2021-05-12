from django.contrib import admin
from .models import Book


# Register your models here.
admin.site.register(Book)#due to this, admin can manage this project

#python code to creat a super user
#python manage.py craetesuperuser
#name:can give any name like dilsha
#email and passwrod also