from django.contrib import admin
from .models import Menu, Page


class MenuAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
