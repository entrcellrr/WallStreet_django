from django.contrib import admin


# Register your models here.
from .models import Share_Data, DynamicShare

class ShareDataAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Share_Data,ShareDataAdmin)

class DynamicShareAdmin(admin.ModelAdmin):
	list_display=["shareName"]
admin.site.register(DynamicShare,DynamicShareAdmin)