from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameho', 'emailho', 'ageho')
    search_fields = ('nameho', 'emailho')

# Register your models here.
