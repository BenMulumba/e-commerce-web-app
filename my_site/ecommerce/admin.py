from django.contrib import admin
from .models import customer,product,Inventory,order

# Register your models here.
admin.site.register(customer)
admin.site.register(product)
admin.site.register(Inventory)
admin.site.register(order)
