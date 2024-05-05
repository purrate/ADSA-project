# Your Streamlit app

import streamlit as st
import datetime
import os
import subprocess
import requests
from time import perf_counter_ns
st.title('Stock Market Price Fetcher')
st.sidebar.title('Navigation')

main_content = st.container()

key = "0QP0P9FHTR9KS16T"

with main_content:
    keyword = st.text_input("Enter a keyword to search for symbols")
    st.write('Please select a date from the calendar below and choose an option from the dropdown menu.')
    
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        symbol_options = [item['1. symbol'] for item in data['bestMatches']]
        selected_symbol = st.selectbox('Choose a symbol:', symbol_options)

    else:
        st.error("Failed to fetch symbol data. Please check your internet connection or try again later.")
    
    d = st.date_input(
        "Select a date",
        datetime.date.today(),
        format="YYYY-MM-DD",
    )
    st.write('The selected date is:', d)
    
    start_time = perf_counter_ns()
    output = subprocess.check_output(['python', 'stockprice2.py', selected_symbol, str(d)])
    end_time = perf_counter_ns()

    st.write("Output from stockprice.py:")
    data = output.decode("utf-8").split("\n")[1].strip("()").split(", ")
    table_data = {item.split(": ")[0].strip("'"): item.split(": ")[1].strip("'") for item in data[1:]}
    st.table([table_data])
    
    st.write(f"Information was fetched in: {(end_time - start_time)/1_000_000} ms")
