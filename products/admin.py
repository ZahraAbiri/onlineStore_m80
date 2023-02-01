from django.contrib import admin

from .models import Products
from .models import Discount
from .models import SuperCategory
from .models import SubCategory
admin.site.register(Products)
admin.site.register(SuperCategory)
admin.site.register(SubCategory)
admin.site.register(Discount)
