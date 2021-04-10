from django.contrib import admin

# Register your models here.
from .models import job , Catagory

admin.site.register(job)

admin.site.register(Catagory)