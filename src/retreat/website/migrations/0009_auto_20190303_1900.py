# Generated by Django 2.1.4 on 2019-03-03 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_attendee_paypal_txn_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendee',
            old_name='blah',
            new_name='paypal_payload',
        ),
    ]
