from django.core.validators import RegexValidator
from django.db import models
from products.models import Products
from django.utils.html import mark_safe
class User(models.Model):
    roles = [
        ('customer', 'customer'),
        ('nazer', 'nazer'),
        ('operator', 'operator'),
        ('admin', 'admin'),
    ]
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    national_code = models.CharField(max_length=10, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+919198989'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)  # validators should be a list
    role = models.CharField(choices=roles, max_length=15)
    email = models.EmailField(null=False, unique=True)
    image = models.ImageField(upload_to="images", max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=8)

    def img_preview(self):  # new
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
    class Meta:
        verbose_name = 'کاربران'

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"


class Address(models.Model):
    city_name = models.CharField(max_length=50, null=False)
    avenue_name = models.CharField(max_length=50, null=False)
    street_name = models.CharField(max_length=50, null=False)
    plate = models.CharField(max_length=3, null=False)
    zipCode = models.CharField(max_length=10, null=False)
    customer = models.ForeignKey(User, verbose_name='customer_id', related_name='customer_id',
                                 on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.city_name + ":" + self.avenue_name + ":" + \
               self.zipCode + ":" + self.plate


class Comments(models.Model):
    description = models.CharField(max_length=150, null=False)
    product = models.ForeignKey(Products, verbose_name='product_id',
                                related_name='product_id',
                                on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, verbose_name='customer_id', related_name='user',
                                 on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description
