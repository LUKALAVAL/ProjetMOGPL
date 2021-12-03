from interp import *
from paths import *
import gurobi as g

G = interp_file('../graphs/testdif.txt')

start = 'A'
end = 'C'
#Pour éviter les retours de lignes cachés
start.strip()
end.strip() 
ts = 1
te = 100
print("\nt1")
t1 = type1(start,end,G,ts,te)
print(t1)

print("\nt2")
t2 = type2(start,end,G,ts,te)
print(t2)

print("\nt3")
t3 = type3(start,end,G,ts,te)
print(t3)

print("\nt4")
t4 = type4(start,end,G,ts,te)
print(t4)

print("\nt4 gurobi")
t4g = g.type4(start,end,G,ts,te)
print(t4g)

G_ = transformT4(start,end,G,ts,te)
s_dep = (start,inf)
for k in G_.keys():
    if k[0] == start and k[1] < s_dep[1]:
        s_dep = k
print("\nTEST BFS")
test = BFS_Min(s_dep, end, G_)
print(test)

