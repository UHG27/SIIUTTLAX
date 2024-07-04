from django.contrib import admin
from .models import Category, Professor, Student

# Register your models here.
admin.site.register(Category)
admin.site.register(Professor)
admin.site.register(Student)

