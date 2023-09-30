from .customer import CustomerListView, CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerUpdateView
from .order import OrderListView, OrderCreateView, OrderDeleteView, OrderDetailView, OrderUpdateView
from .support_tickets import SupportTicketMessageCreateView

__all__ = [
    'CustomerUpdateView',
    'CustomerDetailView',
    'CustomerDeleteView',
    'CustomerCreateView',
    'CustomerListView',
    'OrderUpdateView',
    'OrderDetailView',
    'OrderDeleteView',
    'OrderCreateView',
    'OrderListView',
    'SupportTicketMessageCreateView'
]
