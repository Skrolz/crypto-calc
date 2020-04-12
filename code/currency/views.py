from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Currency

def currencies(request):
    currencies = serializers.serialize('json', Currency.objects.all(), cls=DjangoJSONEncoder)
    title = 'Currencies'
    return render(request, 'currency/base.html', {'currencies':currencies,'title':title})