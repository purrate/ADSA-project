import csv
from fractalTreeServer import FractalTree
import sys

ORDER = 32

tree = FractalTree(order=ORDER)
import os
print(os.getcwd())

DATAFILE = f"./datasets/{sys.argv[1]}"

with open(DATAFILE, "r") as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

for price in data:
    tree.buffer((price["Date"], price, "insert"))

price = tree.search_retrieval(f"{sys.argv[2]}")
print(price)
