from django.contrib import admin

from .models import Link, Menu, Page


class LinkAdmin(admin.ModelAdmin):
    pass


class MenuAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Link, MenuAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Page, PageAdmin)
