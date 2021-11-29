from interp import *
from paths import *
import gurobi as g

G = interp_file('../graphs/test2.txt')

start = 'A'
end = 'L'
ts = 2
te = 10

print("\nt1")
t1 = type1(start,end,G,ts,te)
print(t1)

print("\nt2")
t2 = type2(start,end,G,ts,te)
print(t2)

print("\nt3")
t3 = type3()
print(t3)

print("\nt4")
t4 = type4(start,end,G,ts,te)
print(t4)

print("\nt4 gurobi")
t4g = g.type4(start,end,G,ts,te)
print(t4g)
