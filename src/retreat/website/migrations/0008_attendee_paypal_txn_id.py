# Generated by Django 2.1.4 on 2019-03-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_attendee_blah'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='paypal_txn_id',
            field=models.CharField(default='', max_length=255),
        ),
    ]