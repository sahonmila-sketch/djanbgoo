from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameja', 'emailja', 'ageja')
    search_fields = ('nameja', 'emailja')
    
admin.site.register(UserModel, UserAdmin)
# Register your models here.
