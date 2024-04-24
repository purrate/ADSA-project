import random
from fractalTreeServer import FractalTree
import query
bplustree = FractalTree(order=8)  # fractal tree object
# This is the dummmy data for the Fractal Tree where it takes a key, a dictionary for a value and the operation that needs to be done on it
bplustree.buffer((1, {"Name": "Avvyukt", "Age": "20"}, "insert"))
bplustree.buffer((2, {"Name": "Jey", "Age": "20"}, "insert"))
bplustree.buffer((3, {"Name": "Stg", "Age": "20"}, "insert"))
bplustree.buffer((4, {"Name": "Sidg", "Age": "20"}, "insert"))

print("Reached")
q = query.Query(bplustree)  # query class # takes user input
q.show()  # this shows the data we have put as input as table

message = (4, "delete")
bplustree.buffer(message)
q.show()