from django.db import models


class Attendee(models.Model):
    PAYPAL = 'PP'
    CASH = 'CA'
    PAYMENT_TYPE_CHOICES = (
        (PAYPAL, 'Paypal'),
        (CASH, 'Cash')
    )

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    amount_paid = models.DecimalField(decimal_places=2, max_digits=10)
    phone = models.CharField(null=True, max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE_CHOICES,
        default=PAYPAL
    )

    def __str__(self):
        return self.name
