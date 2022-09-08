import requests
import json
# We will assume that the following link is the link to the API
response = requests.get("https://api.open-notify.org/astros.json")

# We will only parse the data if the response is successful
if response.status_code == 200:
    data = response.json()

    # We will parse the data to calculate monthly balance with income and expenses
    # We will assume that the data is in the following format for certain month
    # data = {
    #     "message": "success",
    #     "number_of_transactions": 4,
    #     "transactions": [
    #         {
    #             "amount": 100,
    #             "type": "income"
    #         },
    #         {
    #             "amount": 50,
    #             "type": "expense"
    #         },
    #         {
    #             "amount": 20,
    #             "type": "income"
    #         },
    #         {
    #             "amount": 10,
    #             "type": "expense"
    #         }
    #     ]
    # }

    # We will calculate the monthly balance using the following formula
    # monthly_balance = income - expenses
    income = sum([transaction["amount"] for transaction in data["transactions"] if transaction["type"] == "income"])
    expenses = sum([transaction["amount"] for transaction in data["transactions"] if transaction["type"] == "expense"])
    monthly_balance = income - expenses

    # We then send the monthly balance to an external API
    response = requests.post("https://api.open-notify.org/astros.json",
                             json={"monthly_balance": monthly_balance, "income": income, "expenses": expenses})

