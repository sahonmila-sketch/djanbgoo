from django.contrib import admin
from .models import UserModel

class UserAdmin(admin.ModelAdmin):
    list_display = ('nameme', 'emailme', 'ageme')
    search_fields = ('nameme', 'emailme')


admin.site.register(UserModel, UserAdmin)



# Register your models here.
