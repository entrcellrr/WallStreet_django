from django.contrib import admin

# Register your models here.
from .models import UserDetail
class UserDetailAdmin(admin.ModelAdmin):
    list_display=["__str__"]
admin.site.register(UserDetail,UserDetailAdmin)