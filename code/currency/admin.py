from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    fieldsets = [
        ('GENERAL', {'fields':[
            'name',
            'abbreviation',
        ]}),
        ('OTHER', {'fields':[
            'comments',
        ]}),
    ]
    list_display = [
        'name',
        'abbreviation',
    ]
    ordering = [
        'name',
    ]
    search_fields = [
        'name',
        'abbreviation',
    ]

admin.site.register(Currency, CurrencyAdmin)