import tkinter as tk
from tkinter import filedialog
import csv
import json
import re
from CsvModels import Transaction, transaction_json

root = tk.Tk()
root.withdraw()
transactions = []
amountlist_ = []

file_path = filedialog.askopenfilename(title="Select File", filetypes=(("CSV Files", "*.csv"),))


def getfloat(_amount_list):
    _amount_list = _amount_list.split(".")
    amount = ""
    for num in _amount_list:
        amount += num
    amount = amount.split(",")
    amount = float(amount[0] + '.' + amount[1])
    return amount


def monthlydiff(_amount_list_):
    mdiff = 0.0
    for num in _amount_list_:
        mdiff = num + mdiff
    return mdiff


with open(file_path) as csv_file:
    csvr = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for column in csvr:
        if line_count == 0:
            print("Monthly difference in income/outcome:")
        elif len(column) > 0:
            date = column[0]
            text = column[1]
            amount = getfloat(column[2])
            amountlist_.append(amount)
            balance = getfloat(column[3])
            status = column[4]
            attuned = column[5]
            transaction = Transaction(
                date,
                text,
                amount,
                balance,
                status,
                attuned
            )
            exists = False
            for transfer in transactions:
                if transfer.date == transaction.date:
                    if transfer.amount == transaction.amount:
                        exists = True
            if exists != True:
                transactions.append(transaction)
        line_count = line_count + 1
    monthlydifference = 0.0
    for number in amountlist_:
        monthlydifference = monthlydifference + number
    print(monthlydifference)


with open('Csvjson.json', 'w') as json_file:
    data = {"Transaction": []}
    for transfers in transactions:
        data["Transaction"].append(transfers.serialize())
    json.dump(data, json_file, sort_keys=False, indent=4, ensure_ascii=False)



#TODO Add more information - highest transaction, place where most money is used, what days are most expensive.