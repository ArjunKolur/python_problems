import requests

url = 'http://data.fixer.io/api/latest?access_key=5b2f9f19aa542b27058de66e1d6c57f6'

def currency_conversion():
    from_currency = input('From country: ')
    to_currency = input('To country: ')
    amount = int(input('Amount: '))

    response = requests.get(url)
    data = response.json()

    if 'rates' in data and from_currency in data['rates']:
        rate = data['rates'][from_currency]
        amount_in_eur = amount / rate
        converted_amount = amount_in_eur * data['rates'][to_currency]
        converted_amount = round(converted_amount, 2)
        print(f'{amount} {from_currency} is equal to {converted_amount} {to_currency}')
    else:
        print('Invalid currency!')

    again = input('Again? (yes/no): ')
    if again.lower() == 'yes':
        currency_conversion()

currency_conversion()
