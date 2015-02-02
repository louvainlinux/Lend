from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from label_generator import generator
from labelling.models import *


def print_label(modeladmin, request, queryset):
    printer_name = Config.objects.get(pk='printer_name')
    printer_uri = Config.objects.get(pk='printer_uri')
    for a in queryset:
        generator.print_label(generator.generate_label(a.id), printer_name.value, printer_uri.value)
print_label.short_description = "Print a label"


class LabelAdmin(admin.ModelAdmin):
    actions = [print_label]
    list_display = ('id', 'name', 'type')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location')


class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'type')


class LendingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'borrower', 'label', 'complete')

admin.site.register(LabelType, MPTTModelAdmin)
admin.site.register(EquipmentType, MPTTModelAdmin)
admin.site.register(BorrowerType, MPTTModelAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Lending, LendingAdmin)
admin.site.register(Config)
