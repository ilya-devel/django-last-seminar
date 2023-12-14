from django.db import models
from django.core.validators import RegexValidator

NEW_ROW = "\n\t"

def change_symb(row: str):
    return row.replace("\n", "\t")

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        # Validators should be a list
        validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=200)
    reg_data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='media/')
    add_data = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    full_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    create_date = models.DateTimeField()
    is_done = models.BooleanField(default=False)

    def set_full_price(self, *args, **kwargs):
        self.full_price = sum([product.price for product in self.products.all()])
        self.save()

    def __str__(self) -> str:
        return f'Order by {self.customer.name}:\nFrom: {self.create_date}\nProducts list:\n\t{NEW_ROW.join([change_symb(str(prod)) for prod in self.products.all()]) if self.products.all() else "empty list"}\n\n\nFull price: {self.full_price}'
