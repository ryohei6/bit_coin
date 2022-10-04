import streamlit as st
from view.call_api import APICaller
from view.process_data import DataProcesser

call_api = APICaller()
process_data = DataProcesser()

def choose_currency_type(currency_list):
    message = "choose your page"
    page = st.sidebar.selectbox(message, currency_list)
    return page

def display_bitcoin_chart():
    st.title("Bitcoin")
    
    bitcoin = call_api.get_annual_currency_data("http://127.0.0.1:8000/read_bitcoin")    
    today_price = call_api.fetch_latest_currency_data("http://127.0.0.1:8000/fetch_bitcoin")
    
    st.write(today_price.text)   
    st.write("bitcoin chart")
    
    df = process_data.get_current_currency_data(bitcoin)
    df = process_data.concat_latest_currency_data(df, today_price)
    
    short_term_value = st.number_input(label="短期の移動平均", value=7, min_value=0, max_value=365)
    long_term_value = st.number_input(label="長期の移動平均", value=30, min_value=0, max_value=365)
    
    df_with_ma = process_data.add_moving_average(df, short_term_value, long_term_value)
    
    st.dataframe(df_with_ma)
    st.line_chart(df_with_ma, x="date", use_container_width=True)    

def display_ethareum_chart():
    st.title("Ethareum")
    st.write("### Now developing")