import requests

def get_exchange_rate():
    r = requests.get("https://api.exchangerate.host/latest")
    return r.json()["rates"]["USD"]

def get_currency_rate(api_client):
    data = api_client.json()
    return data["rate"]

def convert_rubles_to_usd(amount):
    rate = get_exchange_rate()
    return amount / rate

