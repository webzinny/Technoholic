from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display=['id','email','pas','name','dob','gender','contact','contact2']

admin.site.register(Data,DataAdmin)
