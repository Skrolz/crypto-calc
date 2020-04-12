from django.shortcuts import render
from .models import Transaction

def transaction_list(request):
    return render(request, 'transaction/transaction_list.html', {})