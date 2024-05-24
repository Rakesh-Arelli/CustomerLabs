from django.contrib import admin

# Register your models here.
# core/admin.py

from django.contrib import admin
from .models import Account, Destination

admin.site.register(Account)
admin.site.register(Destination)
