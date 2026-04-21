from django.contrib import admin

from .models import Billing, Product, SalesData, SalesInvoice

admin.site.register(Product)
admin.site.register(Billing)
admin.site.register(SalesData)
admin.site.register(SalesInvoice)
