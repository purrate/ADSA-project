from functools import total_ordering
from b_tree import B_Tree
from fractalTreeServer import FractalTree

ORDER = 32
INSERT_LIMIT = 100_000

@total_ordering
class KeyValuePair:

    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __eq__(self, other):
        return self.key == other.key
    

btree = B_Tree(ORDER)
ftree = FractalTree(ORDER)

from time import perf_counter_ns

btree_start = perf_counter_ns()

for i in range(INSERT_LIMIT):
    btree.insert(KeyValuePair(i, i))

btree_end = perf_counter_ns()

elapsed_ms = (btree_end - btree_start) / 1_000_000

print(f"B-Tree insertion of {INSERT_LIMIT} elements took {elapsed_ms} ms")


ftree_start = perf_counter_ns()

for i in range(INSERT_LIMIT):
    ftree.buffer((i, i, "insert"))

ftree_end = perf_counter_ns()

elapsed_ms = (ftree_end - ftree_start) / 1_000_000

print(f"Fractal-Tree insertion of {INSERT_LIMIT} elements took {elapsed_ms} ms")



# btree_start = perf_counter_ns()

# for i in range(INSERT_LIMIT):
#     pair = btree.search(KeyValuePair(i, i))

# btree_end = perf_counter_ns()

# elapsed_ms = (btree_end - btree_start) / 1_000_000

# print(f"B-Tree searching of {INSERT_LIMIT} elements took {elapsed_ms} ms")

# ftree_start = perf_counter_ns()

# for i in range(INSERT_LIMIT):
#     pair = ftree.search_retrieval(i)

# ftree_end = perf_counter_ns()
# elapsed_ms = (ftree_end - ftree_start) / 1_000_000

# print(f"Fractal-Tree searching of {INSERT_LIMIT} elements took {elapsed_ms} ms")


