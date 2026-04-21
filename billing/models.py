from django.db import models


class Product(models.Model):
    product_number = models.CharField(max_length=50, unique=True)
    group = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    stock_value = models.DecimalField(max_digits=12, decimal_places=2)
    stock_profit = models.DecimalField(max_digits=12, decimal_places=2)
    profit = models.DecimalField(max_digits=12, decimal_places=2)
    barcode = models.CharField(max_length=100, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_number} - {self.brand}"


class Billing(models.Model):
    bill_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=150)
    billing_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=30, default="Pending")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.bill_number


class SalesData(models.Model):
    sale_date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales_data")
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.product_number} - {self.sale_date}"


class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField()
    customer_name = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number
