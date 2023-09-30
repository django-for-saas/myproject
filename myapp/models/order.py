from django.db import models


class Order(models.Model):
    customer = models.ForeignKey('myapp.Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
