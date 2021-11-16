from interp import *

f = open('../graphs/test.txt','r')

l1,l2 = interpFile(f)
print(l1)
print(l2)
print(checkGraph(l1,l2))

l1,l2 = interpInput()
print(l1)
print(l2)
print(checkGraph(l1,l2))
