from django.contrib import admin
from .models import Realtor
from django.utils.html import format_html

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'name', 'email', 'is_mvp', 'hire_date')
    list_editable = ('email', 'is_mvp')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 20

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:100px;max-height:100px;border-radius:100%;"/>'.format(obj.photo.url))

admin.site.register(Realtor, RealtorAdmin)