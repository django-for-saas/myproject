from django.db import models


class CustomerPayment(models.Model):
    customer = models.ForeignKey('myapp.Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"${self.amount} Payment by {self.customer.name} on {self.payment_date}"
