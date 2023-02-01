from django.db import models
from django.utils.html import mark_safe

class Discount(models.Model):
    kind = [
        ('daily', 'daily'),
        ('birthDay', 'BirthDay'),
        ('cash', 'cash'),
    ]
    discountKind = models.CharField(choices=kind, max_length=15, null=False)
    persent = models.CharField(max_length=5, null=False)

    def __str__(self):
        return self.discountKind + ":" + self.persent


class SuperCategory(models.Model):
    name = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, null=False)
    superCategory = models.ForeignKey(SuperCategory, verbose_name='superCategory_id', related_name='superCategory_id',
                                      on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ":" + self.superCategory.name


class Products(models.Model):
    Inventory = [
        ('Available', 'Available'),
        ('finished', 'finished'),
    ]
    name = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=255, null=False)
    count = models.IntegerField(null=False)
    productInventory = models.CharField(choices=Inventory, max_length=15, null=False)
    price = models.CharField(max_length=10, null=False)
    image = models.ImageField(upload_to="product_images", max_length=100)
    discount = models.ForeignKey(Discount, verbose_name='discount_id', related_name='discount_id',
                                 on_delete=models.CASCADE, null=True)
    subCategory = models.ForeignKey(SubCategory, verbose_name='subCategory_id', related_name='subCategory_id',
                                    on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'products'
    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
    def __str__(self):
        return f"{self.name}-{self.brand}-{str(self.count)}-{str(self.price)}"
