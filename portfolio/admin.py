from django.contrib import admin


# Register your models here.
from .models import Share_Data

class ShareDataAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Share_Data,ShareDataAdmin)