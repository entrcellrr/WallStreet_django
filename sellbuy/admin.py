from django.contrib import admin


# Register your models here.
from .models import Share,ShareDetail,Timer,News
from .forms import ShareForm

class ShareAdmin(admin.ModelAdmin):
    list_display=["__str__","describ","currentprice","queries"]
    form=ShareForm
admin.site.register(Share,ShareAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display=["__str__","weight"]
admin.site.register(News,NewsAdmin)


class TimerAdmin(admin.ModelAdmin):
	list_display=["name","time"]
admin.site.register(Timer,TimerAdmin)

class ShareDetailAdmin(admin.ModelAdmin):
    list_display=["__str__","money_in_hand"]
admin.site.register(ShareDetail,ShareDetailAdmin)