# Generated by Django 3.0.5 on 2020-04-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_auto_20200408_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='abbreviation',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
