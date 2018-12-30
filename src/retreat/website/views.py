from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Attendee

def index(request):
    return render(request, 'website/index.html')


@csrf_exempt
def ipn(request):
    name = request.POST.get('first_name', '')
    name += ' ' + request.POST.get('last_name', '')
    email = request.POST.get('payer_email')
    amount_paid = request.POST.get('mc_gross')
    amount_paid = float(amount_paid)
    fee = request.POST.get('mc_fee')
    fee = float(fee)
    attendee = Attendee()
    attendee.name = name.strip()
    attendee.email = email
    attendee.amount_paid = amount_paid
    attendee.fee = fee
    attendee.save()
    return HttpResponse()

