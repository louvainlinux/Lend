from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
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
    exclude = ('borrowed',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'location')
    exclude = ('borrowed',)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'type')

class LendingForm(forms.ModelForm):
    class Meta:
        model = Lending

    labels = forms.ModelMultipleChoiceField(queryset=Label.objects.all(),required=False,widget=forms.SelectMultiple)
    equipments = forms.ModelMultipleChoiceField(queryset=Equipment.objects.all(),required=False,widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super(LendingForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['labels'].initial = self.instance.borrowed_labels.all()
            self.fields['equipments'].initial = self.instance.borrowed_equipments.all()

    def save(self, *args, **kwargs):
        instance = super(LendingForm, self).save(commit=False)
        self.fields['labels'].initial.update(borrowed=None)
        self.cleaned_data['labels'].update(borrowed=instance)
        self.fields['equipments'].initial.update(borrowed=None)
        self.cleaned_data['equipments'].update(borrowed=instance)
        return instance

class LendingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start', 'end', 'borrower', 'complete')
    form = LendingForm

admin.site.register(LabelType, MPTTModelAdmin)
admin.site.register(EquipmentType, MPTTModelAdmin)
admin.site.register(BorrowerType, MPTTModelAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Lending, LendingAdmin)
admin.site.register(Config)
