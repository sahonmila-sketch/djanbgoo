from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameke', 'emailke', 'ageke')
    search_fields = ('nameke', 'emailke')

admin.site.register(UserModel, UserAdmin)

# Register your models here.
