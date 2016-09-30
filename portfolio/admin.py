from django.contrib import admin


# Register your models here.
from .models import *
class Xaviers_SchoolAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Xaviers_School,Xaviers_SchoolAdmin)

class Wayne_EnterprisesAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Wayne_Enterprises,Wayne_EnterprisesAdmin)

class Walter_White_IncAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Walter_White_Inc,Walter_White_IncAdmin)

class Umbrella_CorpAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Umbrella_Corp,Umbrella_CorpAdmin)

class STAR_LabsAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(STAR_Labs,STAR_LabsAdmin)

class Stark_IndustriesAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Stark_Industries,Stark_IndustriesAdmin)

class SkynetAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Skynet,SkynetAdmin)

class SHIELDAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(SHIELD,SHIELDAdmin)

class Pearson_HardmanAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Pearson_Hardman,Pearson_HardmanAdmin)

class Palmer_TechAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Palmer_Tech,Palmer_TechAdmin)

class Oscorp_RnDAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Oscorp_RnD,Oscorp_RnDAdmin)

class Olivanders_WandAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Olivanders_Wand,Olivanders_WandAdmin)

class Monsters_IncAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Monsters_Inc,Monsters_IncAdmin)

class LexCorpAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(LexCorp,LexCorpAdmin)

class Illuminati_ConsolidationsAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Illuminati_Consolidations,Illuminati_ConsolidationsAdmin)

class Hammer_TechAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Hammer_Tech,Hammer_TechAdmin)

class Gringotts_BankAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Gringotts_Bank,Gringotts_BankAdmin)

class Evil_IncAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Evil_Inc,Evil_IncAdmin)

class Daily_PlanetAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Daily_Planet,Daily_PlanetAdmin)

class Buzzinga_EntertainmentAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Buzzinga_Entertainment,Buzzinga_EntertainmentAdmin)

class Bajrang_CafeAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Bajrang_Cafe,Bajrang_CafeAdmin)

class Bakers_Street_FindingsAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Bakers_Street_Findings,Bakers_Street_FindingsAdmin)

class Ammunation_PharmaAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(Ammunation_Pharma,Ammunation_PharmaAdmin)

class ACMEAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(ACME,ACMEAdmin)

class User_PortfolioAdmin(admin.ModelAdmin):
	list_display=["x","y"]
admin.site.register(User_Portfolio,User_PortfolioAdmin)
