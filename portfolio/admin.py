from django.contrib import admin


# Register your models here.
from .models import Amazon, Google, Facebook, DynamicShare

class AmazonAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Amazon,AmazonAdmin)

class GoogleAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Google,GoogleAdmin)

class FacebookAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Facebook,FacebookAdmin)

class DynamicShareAdmin(admin.ModelAdmin):
	list_display=["shareName"]
admin.site.register(DynamicShare,DynamicShareAdmin)