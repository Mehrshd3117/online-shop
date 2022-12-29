# Django packages
from django.contrib import admin
# Third party apps
from mptt.admin import DraggableMPTTAdmin
# Local apps
from . import models


admin.site.register(
    models.Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        'child',
    ),
    prepopulated_fields = {'slug': ('name',)},
    list_display_links=(
        'indented_title',
    ),
)
