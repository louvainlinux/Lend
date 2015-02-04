from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey

from label_generator import generator


class LabelType(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Label(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    type = TreeForeignKey('LabelType')
    name = models.CharField(max_length=200)
    notes = models.TextField(default="")
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    contained_by = models.ForeignKey('Label', null=True, blank=True, default=None)
    borrowed = models.ForeignKey('Lending',related_name='borrowed_labels',null=True,blank=True,default=None)

    def __str__(self):
        return "{} {}".format(str(self.id).zfill(6), self.name)


#@receiver(post_save, sender=Label)
#def autoprint(instance, created, **kwargs):
#    printer_name = Config.objects.get(pk='printer_name')
#    printer_uri = Config.objects.get(pk='printer_uri')
#    if created:
#        generator.print_label(generator.generate_label(instance.id), printer_name.value, printer_uri.value)


class EquipmentType(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Equipment(models.Model):
    type = TreeForeignKey(EquipmentType)
    name = models.CharField(max_length=200)
    location = models.ForeignKey('Label')
    notes = models.TextField(default="")
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=True)
    borrowed = models.ForeignKey('Lending',related_name='borrowed_equipments',null=True,blank=True,default=None)

    def __str__(self):
        return self.name


class BorrowerType(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Borrower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    type = TreeForeignKey(BorrowerType)

    def __str__(self):
        return self.name


class Lending(models.Model):
    borrower = models.ForeignKey('Borrower')

    start = models.DateField()
    end = models.DateField(blank=True, null=True, default=None)

    deposit = models.DecimalField(default=50, max_digits=6, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    complete = models.BooleanField(default=False)
    deposit_kept = models.DecimalField(default=None, blank=True, null=True, max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.borrower)+str(self.pk)


class Config(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    value = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
