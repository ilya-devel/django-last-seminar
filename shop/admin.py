from django.contrib import admin
from shop import models


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'reg_data']
    list_filter = ['reg_data']
    ordering = ['name']
    readonly_fields = ['reg_data']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Contacts',
            {
                'classes': ['wide'],
                'fields':['email', 'phone_number', 'address']
            }
        ),
        (
            'Created',
            {
                'classes': ['wide'],
                'fields': ['reg_data']
            }
        )
    ]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'add_data']
    list_filter = ['add_data']
    ordering = ['count', 'name', 'price']
    readonly_fields = ['add_data']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            "About",
            {
                'classes': ['collapse', 'wide'],
                'fields': ['description', 'image']
            }
        ),
        (
            "Price and Count",
            {
                'classes': ['wide'],
                'fields': ['price', 'count']
            }
        ),
        (
            'Created',
            {
                'classes': ['wide'],
                'fields': ['add_data']
            }
        )
    ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'full_price', 'create_date', 'is_done']
    list_filter = ['create_date', 'is_done']
    ordering = ['is_done', 'create_date']
    readonly_fields = ['create_date']
    fieldsets = [
        (
            "Customer",
            {
                'classes':['wide'],
                'fields':['customer']
            }
        ),
        (
            "About",
            {
                'classes': ['collapse', 'wide'],
                'fields': ['products', 'full_price', 'is_done']
            }
        ),
        (
            "Created",
            {
                'classes': ['wide'],
                'fields': ['create_date']
            }
        )

    ]
