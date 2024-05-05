import csv
from fractalTreeServer import FractalTree
import sys
import requests

ORDER = 32

tree = FractalTree(order=ORDER)

key = "0QP0P9FHTR9KS16T"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={sys.argv[1]}&apikey={key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    weekly_data = data['Weekly Time Series']
    
    for week, details in weekly_data.items():
        tree.buffer((week, details, "insert"))
else:
    print("Failed to retrieve data:", response.status_code)

date = "1999-11-12"
price = tree.search_retrieval(f"{sys.argv[2]}")
print(price)
