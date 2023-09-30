from django.contrib import admin
from myapp.models import CustomerPayment


class CustomerPaymentAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomerPayment, CustomerPaymentAdmin)
