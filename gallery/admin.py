from django.contrib import admin
from .models import Gallery


# Register your models here.


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'image',
    )


admin.site.register(Gallery, GalleryAdmin)