from django.contrib import admin 

# Register your models here.
from.models import Order,orderItem
admin.site.register(Order)
admin.site.register(orderItem)
