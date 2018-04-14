from django.contrib import admin

from .models import PartCategory, Part
from .models import BomItem

class PartAdmin(admin.ModelAdmin):

    list_display = ('name', 'IPN', 'description', 'stock', 'category')


class PartCategoryAdmin(admin.ModelAdmin):

    list_display = ('name', 'pathstring', 'description')

class BomItemAdmin(admin.ModelAdmin):
    list_display=('part', 'sub_part', 'quantity')

"""
class ParameterTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'units', 'format')


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('part', 'template', 'value')
"""

admin.site.register(Part, PartAdmin)
admin.site.register(PartCategory, PartCategoryAdmin)
admin.site.register(BomItem, BomItemAdmin)

#admin.site.register(PartParameter, ParameterAdmin)
#admin.site.register(PartParameterTemplate, ParameterTemplateAdmin)
#admin.site.register(CategoryParameterLink)
