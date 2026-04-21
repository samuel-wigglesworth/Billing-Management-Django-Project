from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, TemplateView, UpdateView

from .forms import BillingForm, DateFilterForm, ProductForm, SalesDataForm, SalesInvoiceForm
from .models import Billing, Product, SalesData, SalesInvoice


class DateFilteredListView(LoginRequiredMixin, ListView):
    date_field = "created_at"

    def get_queryset(self):
        queryset = super().get_queryset().order_by(f"-{self.date_field}")
        self.filter_form = DateFilterForm(self.request.GET or None)
        if self.filter_form.is_valid():
            start_date = self.filter_form.cleaned_data.get("start_date")
            end_date = self.filter_form.cleaned_data.get("end_date")
            if start_date:
                queryset = queryset.filter(**{f"{self.date_field}__gte": start_date})
            if end_date:
                queryset = queryset.filter(**{f"{self.date_field}__lte": end_date})
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date_filter_form"] = getattr(self, "filter_form", DateFilterForm())
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "billing/dashboard.html"


class ProductListView(DateFilteredListView):
    model = Product
    template_name = "billing/product/list.html"
    context_object_name = "products"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "billing/product/add.html"
    success_url = reverse_lazy("product_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "billing/product/edit.html"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "billing/common/delete_confirm.html"
    success_url = reverse_lazy("product_list")


class BillingListView(DateFilteredListView):
    model = Billing
    template_name = "billing/billing/list.html"
    context_object_name = "bills"
    date_field = "billing_date"


class BillingCreateView(LoginRequiredMixin, CreateView):
    model = Billing
    form_class = BillingForm
    template_name = "billing/billing/add.html"
    success_url = reverse_lazy("billing_list")


class BillingUpdateView(LoginRequiredMixin, UpdateView):
    model = Billing
    form_class = BillingForm
    template_name = "billing/billing/edit.html"
    success_url = reverse_lazy("billing_list")


class BillingDeleteView(LoginRequiredMixin, DeleteView):
    model = Billing
    template_name = "billing/common/delete_confirm.html"
    success_url = reverse_lazy("billing_list")


class SalesDataListView(DateFilteredListView):
    model = SalesData
    template_name = "billing/salesdata/list.html"
    context_object_name = "sales_data"
    date_field = "sale_date"


class SalesDataCreateView(LoginRequiredMixin, CreateView):
    model = SalesData
    form_class = SalesDataForm
    template_name = "billing/salesdata/add.html"
    success_url = reverse_lazy("salesdata_list")


class SalesDataUpdateView(LoginRequiredMixin, UpdateView):
    model = SalesData
    form_class = SalesDataForm
    template_name = "billing/salesdata/edit.html"
    success_url = reverse_lazy("salesdata_list")


class SalesDataDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesData
    template_name = "billing/common/delete_confirm.html"
    success_url = reverse_lazy("salesdata_list")


class SalesInvoiceListView(DateFilteredListView):
    model = SalesInvoice
    template_name = "billing/salesinvoice/list.html"
    context_object_name = "invoices"
    date_field = "invoice_date"


class SalesInvoiceCreateView(LoginRequiredMixin, CreateView):
    model = SalesInvoice
    form_class = SalesInvoiceForm
    template_name = "billing/salesinvoice/add.html"
    success_url = reverse_lazy("salesinvoice_list")


class SalesInvoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = SalesInvoice
    form_class = SalesInvoiceForm
    template_name = "billing/salesinvoice/edit.html"
    success_url = reverse_lazy("salesinvoice_list")


class SalesInvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesInvoice
    template_name = "billing/common/delete_confirm.html"
    success_url = reverse_lazy("salesinvoice_list")
