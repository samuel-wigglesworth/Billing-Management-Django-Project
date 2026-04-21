from django import forms

from .models import Billing, Product, SalesData, SalesInvoice


class DateFilterForm(forms.Form):
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={"type": "date"}))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_number",
            "group",
            "brand",
            "size",
            "min_price",
            "purchase_price",
            "sale_price",
            "stock",
            "stock_value",
            "stock_profit",
            "profit",
            "barcode",
        ]


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ["bill_number", "customer_name", "billing_date", "total_amount", "status"]
        widgets = {"billing_date": forms.DateInput(attrs={"type": "date"})}


class SalesDataForm(forms.ModelForm):
    class Meta:
        model = SalesData
        fields = ["sale_date", "product", "quantity", "unit_price", "total_price"]
        widgets = {"sale_date": forms.DateInput(attrs={"type": "date"})}


class SalesInvoiceForm(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = ["invoice_number", "invoice_date", "customer_name", "amount", "notes"]
        widgets = {"invoice_date": forms.DateInput(attrs={"type": "date"})}
