from django.contrib import admin

from .models import DocumentRelease


admin.site.register(
    DocumentRelease,
    list_display=['version', 'lang', 'scm_url', 'is_default'],
    list_editable=['is_default'],
)
