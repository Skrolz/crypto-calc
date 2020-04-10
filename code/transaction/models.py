from django.db import models
from django.utils import timezone


class Transaction(models.Model):

    # category
    BUY = '1buy'
    SELL = '2sell'
    TRADE = '3trade'
    TRANSFER = '4transfer'
    EARNED = '5earn'
    CATEGORY_CHOICES = (
        (BUY, 'Buy'),
        (SELL, 'Sell'),
        (TRADE, 'Trade'),
        (TRANSFER, 'Transfer'),
        (EARNED, 'Earn'),
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
    currency_in_quantity = models.IntegerField(
        blank=False,
        default=0,
        null=False,
        verbose_name='Quantity'
    )

    # currency IN type
    currency_in_type = models.ForeignKey(
        'currency.Currency',
        models.PROTECT,
        blank=False,
        default=None,
        null=False,
        related_name='currency_in_type',
        verbose_name='Currency'
    )

    # currency OUT quantity
    currency_out_quantity = models.IntegerField(
        blank=False,
        default=0,
        null=False,
        verbose_name='Quantity'
    )

    # currency OUT type
    currency_out_type = models.ForeignKey(
        'currency.Currency',
        models.PROTECT,
        blank=False,
        default=None,
        null=False,
        related_name='currency_out_type',
        verbose_name='Currency'
    )

    # fee quantity
    fee_quantity = models.IntegerField(
        blank=True,
        default=0,
        null=True,
        verbose_name='Quantity'
    )

    # fee type
    fee_type = models.ForeignKey(
        'currency.Currency',
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
        return self.timestamp