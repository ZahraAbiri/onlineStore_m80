from django.db import models

from products.models import Products
from users.models import User


class Orders(models.Model):
    count = models.IntegerField(null=False)
    # sum_price = models.CharField(max_length=10, null=False)
    product =  models.ForeignKey(Products, verbose_name='pro_id', related_name='pro_id',
                                 on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, verbose_name='cus_id', related_name='cus_id',
                                 on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'ordes'

    def __str__(self):
        return self.product.name + ":" + str(self.count)