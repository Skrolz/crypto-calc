from django.shortcuts import render

def transactions(request):
    title = 'Transactions'
    return render(request, 'transaction/base.html',{'title':title})