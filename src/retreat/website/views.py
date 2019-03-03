import boto3
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Attendee


def index(request):
    return render(request, 'website/index.html')


@csrf_exempt
def ipn(request):
    if request.method == 'POST':
        txn_id = request.POST.get('txn_id', '')
        if Attendee.objects.filter(paypal_txn_id=txn_id).exists():
            return HttpResponse()

        name = request.POST.get('item_name', '')
        payer_name = request.POST.get('first_name', '')
        payer_name += ' ' + request.POST.get('last_name', '')
        email = request.POST.get('payer_email')
        amount_paid = request.POST.get('mc_gross')
        amount_paid = float(amount_paid)
        fee = request.POST.get('mc_fee')
        fee = float(fee)

        attendee = Attendee()
        attendee.name = name
        attendee.payer_name = payer_name.strip()
        attendee.email = email
        attendee.amount_paid = amount_paid
        attendee.paypal_txn_id = txn_id
        attendee.fee = fee
        attendee.paypal_payload = json.dumps(request.POST)

        client = boto3.client('sns', region_name='us-east-1')
        topic_arn = client.create_topic(Name='retreat-signup')['TopicArn']
        client.publish(
            TopicArn=topic_arn,
            Message='{} signed up for the retreat'.format(attendee.name)
        )

        attendee.save()
    return HttpResponse()
