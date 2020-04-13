import csv
from transaction.models import Transaction

def import_csv():

    with open('binance.csv') as csv_file:
        line = 0
        file_reader = csv.DictReader(csv_file, delimite',', quotechar='"')
        for row in file_reader:
            line += 1
            print(f'Asset line:{line}')

        transaction = Transaction()
        transaction.category = row['']
        transaction.currency_in_type = row['']
        transaction.currency_in_quantity = row['']
        transaction.currency_out_type = row['']
        transaction.currency_out_quantity = row['']
        transaction.fee_type = row['']
        transaction.fee_quantity = row['']
        transaction.timestamp = row['']
        transaction.comments = row['']

        transaction.full_clean()
        # transaction.save()