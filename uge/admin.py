from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameug', 'emailug', 'ageug')

admin.site.register(UserModel, UserAdmin)
# Register your models here.
