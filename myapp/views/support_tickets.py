from django.views.generic import CreateView
from myapp.models import SupportTicketMessage


class SupportTicketMessageCreateView(CreateView):
    model = SupportTicketMessage
    fields = ['message']
    template_name = 'support_ticket/supportticketmessage_form.html'

    def form_valid(self, form):
        form.instance.ticket_id = self.kwargs['ticket_id']
        form.instance.sender = self.request.user
        return super().form_valid(form)
