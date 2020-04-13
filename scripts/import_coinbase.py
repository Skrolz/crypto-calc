import csv
from decimal import Decimal
from currency.models import Currency
from transaction.models import Transaction

def import_csv():

    with open('coinbase.csv') as csv_file:
        line = 0
        file_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        for row in file_reader:
            line += 1
            print(f'Asset line:{line}')

            for value in row:
                if row[value] == '':
                    row[value] = None
            
            transaction = Transaction()

            # Buy
            if row['Transaction Type'] == 'Buy':
                transaction.category = Transaction.BUY
                transaction.currency_in_type = Currency.objects.get(abbreviation='USD')
                transaction.currency_in_quantity = row['USD Subtotal']
                transaction.currency_out_type = Currency.objects.get(abbreviation=row['Asset'])
                transaction.currency_out_quantity = row['Quantity Transacted']
                transaction.fee_type = Currency.objects.get(abbreviation='USD')
                transaction.fee_quantity = row['USD Fees']

            # Coinbase Earn
            if row['Transaction Type'] == 'Coinbase Earn':
                transaction.category = Transaction.EARN
                transaction.currency_out_type = Currency.objects.get(abbreviation=row['Asset'])
                transaction.currency_out_quantity = row['Quantity Transacted']

            # Convert
            if row['Transaction Type'] == 'Convert':
                transaction.category = Transaction.TRADE
                transaction.currency_in_type = Currency.objects.get(abbreviation=row['Asset'])
                transaction.currency_in_quantity = row['Quantity Transacted']
                transaction.currency_out_type = Currency.objects.get(abbreviation=row['Notes'][-3:])
                transaction.currency_out_quantity = Decimal(row['Notes'][-15:-4])


            # Receive / Send
            if row['Transaction Type'] == 'Receive' or row['Transaction Type'] == 'Send':
                transaction.category = Transaction.TRANSFER
                transaction.currency_in_type = Currency.objects.get(abbreviation=row['Asset'])
                transaction.currency_in_quantity = row['Quantity Transacted']
                transaction.currency_out_type = Currency.objects.get(abbreviation=row['Asset'])
                transaction.currency_out_quantity = row['Quantity Transacted']

            transaction.timestamp = row['Timestamp']
            transaction.comments = row['Notes']

            transaction.full_clean()
            # transaction.save()