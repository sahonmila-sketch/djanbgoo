from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username3', 'email3')
    search_fields = ('username3', 'email3')

admin.site.register(UserModel, UserAdmin)
# Register your models here.
