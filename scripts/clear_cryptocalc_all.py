from transaction.models import Transaction

def clear_cryptocalc():
    Transaction.objects.all().delete()
    print("Crypto-Calc Transactions CLEARED!")