from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from myapp.models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'myapp/customer/customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'myapp/customer/customer_detail.html'


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'myapp/customer/customer_form.html'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name', 'email', 'phone_number', 'address']
    template_name = 'myapp/customer/customer_form.html'


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')
