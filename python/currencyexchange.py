from openexchangerate import OpenExchangeRates

client=OpenExchangeRates(api_key="5ee52ffe26014e5aa3901fa35631fcf5")

#print(client.currencies())

print(client.latest())
