from django.db import models

from goods.models import Product
from users.models import User


class Order(models.Model):
    STATUS_CHOICES = {
        'new': 'Новый',
        'processing': 'В обработке',
        'completed': 'Завершен'
    }

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    status = models.CharField(choices=STATUS_CHOICES, default=STATUS_CHOICES['new'])
    total_amount = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Итоговая стоимость')


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
