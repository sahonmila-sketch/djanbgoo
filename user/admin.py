from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'name', 'surname']

# Register your models here.
admin.site.register(UserModel, UserAdmin)