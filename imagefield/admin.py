from django.contrib import admin
from .models import TableThree
# Register your models here.


from django.contrib import admin
from django.utils.html import format_html

@admin.register(TableThree)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['image_thumbnail']
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    image_thumbnail.short_description = 'Image'
