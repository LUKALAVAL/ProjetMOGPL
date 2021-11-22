from interp import *
from gurobi import *

f = open('../graphs/test2.txt','r')

# l1,l2 = interpFile(f)
# print(l1)
# print(l2)
# print(checkGraph(l1,l2))
#
# l1,l2 = interpInput()
# print(l1)
# print(l2)
# print(checkGraph(l1,l2))

t4 = type4('A','F',interpFile(f))
print(t4)
