from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100,db_index=True)

    class Meta:
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=255)
    cost = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    man = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

