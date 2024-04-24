# Your Streamlit app

import streamlit as st
import datetime
import os
import subprocess
from time import perf_counter_ns

st.title('Stock Market Price Fetcher')
st.sidebar.title('Navigation')

main_content = st.container()

with main_content:
    st.write('Please select a date from the calendar below and choose an option from the dropdown menu.')
    
    dataset_folder = './datasets'
    csv_files = [f for f in os.listdir(dataset_folder) if f.endswith('.csv')]
    selected_dataset = st.selectbox('Choose a dataset:', csv_files)
    st.write('You selected:', selected_dataset)
    
    d = st.date_input(
        "Select a date",
        datetime.date.today(),
        format="YYYY-MM-DD",
    )
    st.write('The selected date is:', d)
    
    start_time = perf_counter_ns()
    output = subprocess.check_output(['python', 'stockprice.py', selected_dataset, str(d)])
    end_time = perf_counter_ns()

    st.write("Output from stockprice.py:")
    data = output.decode("utf-8").split("\n")[1].strip("()").split(", ")
    table_data = {item.split(": ")[0].strip("'"): item.split(": ")[1].strip("'") for item in data[1:]}
    st.table([table_data])
    
    st.write(f"Information was fetched in: {(end_time - start_time)/1_000_000} ms")
