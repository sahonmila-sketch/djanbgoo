from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'namebo', 'surnamebo', 'agebo')

# Register your models here.
