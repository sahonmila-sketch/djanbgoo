from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('namee', 'emailne', 'agene')
    

admin.site.register(UserModel, UserAdmin)

# Register your models here.
