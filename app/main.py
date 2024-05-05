import requests
import pandas as pd

key = "0QP0P9FHTR9KS16T"
symbol = 'MSF0.FRK'

# Construct the API request URL
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={key}'

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
    
    # Extract weekly stock data (adjust keys as per API response structure)
    weekly_data = data['Weekly Time Series']
    
    # Process the data as needed
    for week, details in weekly_data.items():
        print("Week:", week)
        print("Open:", details['1. open'])
        print("High:", details['2. high'])
        print("Low:", details['3. low'])
        print("Close:", details['4. close'])
        print("Volume:", details['5. volume'])
        print("Adjusted Close:", details['5. volume'])
else:
    print("Failed to retrieve data:", response.status_code)