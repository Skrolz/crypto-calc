from django.db import models
from django.utils import timezone
from currency.models import Currency


class Transaction(models.Model):

    # category
    BUY = '1buy'
    SELL = '2sell'
    TRADE = '3trade'
    TRANSFER = '4transfer'
    EARN = '5earn'
    CATEGORY_CHOICES = (
        (BUY, 'Buy'),
        (SELL, 'Sell'),
        (TRADE, 'Trade'),
        (TRANSFER, 'Transfer'),
        (EARN, 'Earn'),
    )
    category = models.CharField(
        blank=False,
        choices=CATEGORY_CHOICES,
        default=BUY,
        max_length=10,
        null=False,
    )

    # comments
    comments = models.TextField(
        blank=True,
        null=True,
    )

    # currency IN quantity
    currency_in_quantity = models.DecimalField(
        blank=True,
        decimal_places=20,
        default=0,
        max_digits=40,
        null=True,
        verbose_name='Quantity'
    )

    # currency IN type
    currency_in_type = models.ForeignKey(
        Currency,
        models.PROTECT,
        blank=True,
        default=None,
        null=True,
        related_name='currency_in_type',
        verbose_name='Currency'
    )

    # currency OUT quantity
    currency_out_quantity = models.DecimalField(
        blank=True,
        decimal_places=20,
        default=0,
        max_digits=40,
        null=True,
        verbose_name='Quantity'
    )

    # currency OUT type
    currency_out_type = models.ForeignKey(
        Currency,
        models.PROTECT,
        blank=True,
        default=None,
        null=True,
        related_name='currency_out_type',
        verbose_name='Currency'
    )

    # fee quantity
    fee_quantity = models.DecimalField(
        blank=True,
        decimal_places=20,
        default=0,
        max_digits=40,
        null=True,
        verbose_name='Quantity'
    )

    # fee type
    fee_type = models.ForeignKey(
        Currency,
        models.PROTECT,
        blank=True,
        default=None,
        null=True,
        related_name='fee_type'
    )

    # timestamp
    timestamp = models.DateTimeField(
        blank=False,
        default=None,
        null=False,
    )

    def __str__(self):
        return str(self.timestamp)