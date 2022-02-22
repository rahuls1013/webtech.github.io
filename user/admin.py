from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')

admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('cname','cpic','cdate')

admin.site.register(category,categoryAdmin)

