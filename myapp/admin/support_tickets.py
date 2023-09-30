from django.contrib import admin
from myapp.models import SupportTicket, SupportTicketMessage


class SupportTicketMessageInline(admin.TabularInline):
    model = SupportTicketMessage


class SupportTicketAdmin(admin.ModelAdmin):
    inlines = [SupportTicketMessageInline]


admin.site.register(SupportTicket, SupportTicketAdmin)
