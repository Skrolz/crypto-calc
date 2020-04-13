# Generated by Django 3.0.5 on 2020-04-12 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0004_auto_20200412_1547'),
        ('transaction', '0005_auto_20200412_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='currency_in_quantity',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=40, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency_in_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency_in_type', to='currency.Currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency_out_quantity',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=40, null=True, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency_out_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='currency_out_type', to='currency.Currency', verbose_name='Currency'),
        ),
    ]