from typing import Any
from django.core.management import BaseCommand, CommandParser
from shop.models import Customer, Product, Order


class Command(BaseCommand):
    help = 'Fill DB'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--customer_id', type=int, required=True, help='Customer ID')
        parser.add_argument('--products_id', type=int, required=True, nargs='+', help='Id products')

    def handle(self, *args: Any, **options: Any) -> str | None:
        customer = Customer.objects.filter(pk=options['customer_id']).first()
        order = Order(
            customer=customer,
        )
        order.save()
        products = []
        for product in options['products_id']:
            item = Product.objects.filter(pk=product).first()
            products.append(item)
        order.products.add(*products)
        order.save()
        order.set_full_price()
        self.stdout.write(f'{order}')
