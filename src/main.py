from interp import *
from paths import *

G = interp_file('../graphs/test2.txt')

print("\nt1")
t1 = type1('A','I',G)
print(t1)

print("\nt2")
t2 = type2('A','I',G)
print(t2)

print("\nt3")
t3 = type3()
print(t3)

print("\nt4")
t4 = type4('A','I',G)
print(t4)
