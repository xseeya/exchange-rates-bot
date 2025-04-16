from config import API_KEY
import requests

class Api:
    def __init__(self):
        self.base_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'
        self.headers = {'apikey':f'{API_KEY}'}
        
    def usd(self):
        result = requests.get(f'{self.base_url}&currencies=RUB&base_currency=USD', headers=self.headers).json()['data']['RUB']
        return f'1 USD - {round(result, 2)} RUB'
    
    def eur(self):
        result = requests.get(f'{self.base_url}&currencies=RUB&base_currency=EUR', headers=self.headers).json()['data']['RUB']
        return f'1 EUR - {round(result, 2)} RUB'
    
    def cny(self):
        result = requests.get(f'{self.base_url}&currencies=RUB&base_currency=CNY', headers=self.headers).json()['data']['RUB']
        return f'1 CNY - {round(result, 2)} RUB'