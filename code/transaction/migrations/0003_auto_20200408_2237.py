# Generated by Django 3.0.5 on 2020-04-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20200408_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('1buy', 'Buy'), ('2sell', 'Sell'), ('3trade', 'Trade'), ('4transfer', 'Transfer'), ('5earned', 'Earned')], default='1buy', max_length=10),
        ),
    ]
