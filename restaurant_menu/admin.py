from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")


admin.site.register(Item, MenuItemAdmin)
