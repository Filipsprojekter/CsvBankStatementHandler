import datetime

class Transaction:
    def __init__(self, date, text, amount, balance, status, attuned):
        self.date = date
        self.text = text
        self.amount = amount
        self.balance = balance
        self.status = status
        self.attuned = attuned

    def serialize(self):
        return {
        "date": self.date,
        "text": self.text,
        "amount": self.amount,
        "balance": self.balance,
        "status": self.status,
        "attuned": self.attuned
        }


def transaction_json(json):
    return Transaction(
        json["date"],
        json["text"],
        json["amount"],
        json["balance"],
        json["status"],
        json["attuned"]
    )
