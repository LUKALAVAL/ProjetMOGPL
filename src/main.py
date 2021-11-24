from interp import *
from transformation import *

graph = transform(interp_file('../graphs/test.txt'))
for s,v in graph.items():
    print(s,v)

# l1,l2 = interp_input()
# print(l1)
# print(l2)
# print(check_graph(l1,l2))
