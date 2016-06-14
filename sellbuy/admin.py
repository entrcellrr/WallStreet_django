from django.contrib import admin


# Register your models here.
from .models import Share
from .models import ShareDetail
from .forms import ShareForm

class ShareAdmin(admin.ModelAdmin):
    list_display=["__str__","describ","currentprice"]
    form=ShareForm
admin.site.register(Share,ShareAdmin)

class ShareDetailAdmin(admin.ModelAdmin):
    list_display=["__str__"]
admin.site.register(ShareDetail,ShareDetailAdmin)