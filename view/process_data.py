import datetime
import pandas as pd
import streamlit as st

class DataProcesser:
    def __init__(self):
        pass
    
    def get_current_currency_data(self, currency):
        df = pd.DataFrame(currency)
        df.columns = ["date", "price"]
        return df
    
    def concat_latest_currency_data(self, df, today_price):
        today = datetime.date.today()
        today = str(today.year)+"年"+str(today.month)+"月"+str(today.day)+"日"
        
        df_insert = pd.DataFrame(
        data={'date': [today], 
              'price': [int(today_price.text)],
              }
        )
        df = pd.concat([df_insert, df])
        
        return df
    
    def add_moving_average(self, df, short_term_value, long_term_value):    
        df["shortMA"] = df["price"].rolling(short_term_value).mean().round(0)
        df["longMA"] = df["price"].rolling(long_term_value).mean().round(0)
        
        return df