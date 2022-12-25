import requests
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/73ae658a3b56b79678d97a0819cdfd99/flightDeals/users"

print("Welcome to Darko's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email_1 = input("What is your email?\n")
email_2 = input("Type your email again.\n")
if email_1 == email_2 :
    print("You are in club.")
    email = email_1

    body = {
        "user":
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
    }
    response = requests.post(url=SHEETY_PRICES_ENDPOINT, json=body)

else:
    print("Different emails.")
