import csv
import gspread
import time

MONTH = 'february'

file = f"chase_{MONTH}.csv"

transactions = []

def chaseFin(file):
    sum = 0
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[1]
            name = row[2]
            amount = float(row[3])
            sum += amount
            category = 'all'
            transaction = ((date, name, amount, category))

            print(transaction)
            transactions.append(transaction)
        return(transactions)

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = chaseFin(file)

for row in rows:
    wks.insert_row([row[0], row[1], row[3], row[2]], 8)
    time.sleep(2)