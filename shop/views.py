from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from shop.models import Customer, Product, Order
from django.utils import timezone
from datetime import timedelta

timedelta()

def week():
    return timezone.now() - timedelta(days=7)

def month():
    return timezone.now() - timedelta(days=30)

def year():
    return timezone.now() - timedelta(days=365)

def get_tuple_products(query_set: Order):
    lst = []
    for order in query_set:
        for product in order.products.all():
            lst.append(product.name)
    return set(lst)


class TemplCustomers(TemplateView):
    template_name = 'shop/users.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['customers'] = Customer.objects.all()
        return context


class TemplateInfoAboutOrders(TemplateView):
    template_name = 'shop/products_of_customer.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(customer=context['customer_id'], create_date__gte=month())
        context['day7'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], create_date__gte=week()))
        context['day30'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], create_date__gte=month()))
        context['day365'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], create_date__gte=year()))
        context['orders'] = orders

        return context
