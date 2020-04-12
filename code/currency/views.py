from django.shortcuts import render
from .models import Currency

def currency_list(request):
    currencies = Currency.objects.all().order_by('abbreviation')
    return render(request, 'currency/currency.html', {'currencies': currencies})