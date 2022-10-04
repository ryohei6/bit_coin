import requests
from bs4 import BeautifulSoup

class DataFetcher():
    def __init__(self):
        self.bitcoin_url = "https://jp.investing.com/crypto/bitcoin/btc-jpy-historical-data"
        pass
    
    def fetch_html(self, url):
        res = requests.get(url)
        html = BeautifulSoup(res.text, 'html.parser')
        return html
        
    def fetch_bitcoin_price(self):
        html = self.fetch_html(self.bitcoin_url)
        latest_value_str = html.find('span', class_='text-2xl').text.replace(",", "")
        latest_value = int(latest_value_str)
        return latest_value
    