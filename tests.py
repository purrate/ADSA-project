import random
from fractalTreeServer import FractalTree
#import query
tree = FractalTree(order=4)  # fractal tree object

kv_pairs = [
    (21, "Avyyukt"),
    (102, "Jeya"),
    (20, "Avishek"),
    (2, "Abhay"),
    (1, "Aadit"),
    (129, "Thomas")
]

for k, v in kv_pairs:
    tree.buffer((k, v, "insert"))

tree.buffer((2, "delete"))
#print(tree.search_retrieval(2))


