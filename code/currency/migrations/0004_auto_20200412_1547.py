# Generated by Django 3.0.5 on 2020-04-12 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_auto_20200409_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'currencies'},
        ),
    ]