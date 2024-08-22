from django.contrib import admin
from .models import Shirt, Shop
# Register your models here.

class ShirtAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'size')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('shirt',)
    

admin.site.register(Shirt, ShirtAdmin)
admin.site.register(Shop, ShopAdmin)
