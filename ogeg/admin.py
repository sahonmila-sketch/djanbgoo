from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameeg', 'emaileg', 'ageeg')
    search_fields = ('nameeg', 'emaileg')

admin.site.register(UserModel, UserAdmin)

# Register your models here.
