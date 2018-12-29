from django.contrib import admin
from .models import Attendee


class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'amount_paid', 'payment_type', 'creation_date')


admin.site.register(Attendee, AttendeeAdmin)
