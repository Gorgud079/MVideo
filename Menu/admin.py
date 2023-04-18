from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *


class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20

admin.site.register(MenuItem, MenuItemMPTTModelAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductCategory)
