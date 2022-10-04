import requests

class APICaller:
    def __init__(self):
        pass
    
    def get_annual_currency_data(self, url):
        res = requests.get(url)
        bitcoin = res.json()
        return bitcoin
    
    def fetch_latest_currency_data(self, url):
        today_price = requests.get(url)
        return today_price