from django.contrib import admin
from . import models

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(models.Page, PageAdmin)