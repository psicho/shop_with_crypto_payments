from django.db import models
from shop.models import Product
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(verbose_name=_('Имя'), max_length=50)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=50)
    email = models.EmailField()
    address = models.CharField(verbose_name=_('Адрес'), max_length=250)
    postal_code = models.CharField(verbose_name=_('Индекс'), max_length=20)
    city = models.CharField(verbose_name=_('Город'), max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    ethereum_wallet = models.CharField(verbose_name=_('Ethereum wallet (кошелёк с которого '
                                                      'будет производиться оплата заказа)'), max_length=50)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
