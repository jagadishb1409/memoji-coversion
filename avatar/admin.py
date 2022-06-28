from django.contrib import admin
from .models import Gender, SkinColor, ClothingColor, HairColor, HairType, FacialHairType, Accessory, ClothingType
# Register your models here.

admin.site.register(Gender)
admin.site.register(SkinColor)
admin.site.register(ClothingColor)
admin.site.register(HairColor)
admin.site.register(HairType)
admin.site.register(FacialHairType)
admin.site.register(Accessory)
admin.site.register(ClothingType)