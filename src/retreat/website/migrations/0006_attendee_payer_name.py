# Generated by Django 2.1.4 on 2019-03-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_attendee_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='payer_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]