from django.db import models

class Payment(models.Model):
    """ "PaymentMethod"""
    order = models.CharField(max_length=100, verbose_name='Order')
    user = models.CharField(max_length=100, verbose_name='User')
    payment_method = models.CharField(
        max_length=100, default='PAYPAL', verbose_name='Payment Method')
    payment_status = models.BooleanField(
        default=False, verbose_name='Is Paid ?')
    amount = models.DecimalField(
        decimal_places=2, max_digits=50, verbose_name='Amount')
    currency = models.CharField(max_length=200, default='USD')

    class Meta:
        unique_together = (('order', 'payment_status'),)
        indexes = [models.Index(fields=["payment_method"])]

    def __str__(self):
        return self.amount