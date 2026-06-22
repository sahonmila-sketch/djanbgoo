from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username5', 'email5')
    search_fields = ('username5', 'email5')

# Register your models here.
