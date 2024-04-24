import csv
from fractalTreeServer import FractalTree

ORDER = 32

tree = FractalTree(order=ORDER)  # fractal tree object
import os
print(os.getcwd())

DATAFILE = "datasets/ADANIPORTS.csv"

with open(DATAFILE, "r") as f:
    # csv.DictReader uses first row for column names by default
    reader = csv.DictReader(f)
    data = [row for row in reader]

for price in data:
    tree.buffer((price["Date"], price, "insert"))

price = tree.search_retrieval("2007-11-27")
print(price)
