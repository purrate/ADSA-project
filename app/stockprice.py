import csv
from fractalTreeServer import FractalTree
import sys

ORDER = 32

tree = FractalTree(order=ORDER)  # fractal tree object
import os
print(os.getcwd())

DATAFILE = f"./datasets/{sys.argv[1]}"

with open(DATAFILE, "r") as f:
    # csv.DictReader uses first row for column names by default
    reader = csv.DictReader(f)
    data = [row for row in reader]

for price in data:
    tree.buffer((price["Date"], price, "insert"))

price = tree.search_retrieval(f"{sys.argv[2]}")
print(price)
