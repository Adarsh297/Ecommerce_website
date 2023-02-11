from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)