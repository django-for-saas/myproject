from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from myapp.models import Order


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
