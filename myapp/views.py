from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SupportTicketMessage, Order
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'customer/customer_form.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'customer/customer_form.html'


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'


class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'order_date', 'total_amount']
    template_name = 'order/order_form.html'


class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer', 'order_date', 'total_amount']
    template_name = 'order/order_form.html'


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order-list')


class SupportTicketMessageCreateView(CreateView):
    model = SupportTicketMessage
    fields = ['message']
    template_name = 'support_ticket/supportticketmessage_form.html'

    def form_valid(self, form):
        form.instance.ticket_id = self.kwargs['ticket_id']
        form.instance.sender = self.request.user
        return super().form_valid(form)
