from django.core import serializers
from django.shortcuts import render
from .models import Transaction

def transactions(request):
    transactions = serializers.serialize('json', Transaction.objects.all(),use_natural_foreign_keys=True)
    title = 'Transactions'
    return render(request, 'transaction/base.html',{'transactions':transactions,'title':title})