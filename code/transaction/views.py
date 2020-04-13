from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from .models import Transaction

def transactions(request):
    transactions = serializers.serialize('json', Transaction.objects.all(), cls=DjangoJSONEncoder)
    title = 'Transactions'
    return render(request, 'transaction/base.html',{'transactions':transactions,'title':title})