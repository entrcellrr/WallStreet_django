from django.contrib import admin


# Register your models here.
from .models import Share
from .models import ShareDetail
from .models import Timer
from .forms import ShareForm

class ShareAdmin(admin.ModelAdmin):
    list_display=["__str__","describ","currentprice","queries"]
    form=ShareForm
admin.site.register(Share,ShareAdmin)

class TimerAdmin(admin.ModelAdmin):
	list_display=["name","time"]
admin.site.register(Timer,TimerAdmin)

class ShareDetailAdmin(admin.ModelAdmin):
    list_display=["__str__"]
admin.site.register(ShareDetail,ShareDetailAdmin)