from interp import *
from paths import *
import gurobi as g

G = interp_file('../graphs/test3.txt')

start = 'A'
end = 'G'
#Pour éviter les retours de lignes cachés
start.strip()
end.strip() 
ts = 1
te = 100
print("\nt1")
t1 = type1(start,end,G,ts,te)
print(t1)

print("\nt1 BFS")
t1BFS = type1_BFS(start, end,G, ts, te)
print(t1BFS)

print("\nt2")
t2 = type2(start,end,G,ts,te)
print(t2)
print("\nt2 BFS")
t2BFS = type2_BFS(start, end,G, ts, te)
print(t2BFS)

print("\nt3")
t3 = type3(start,end,G,ts,te)
print(t3)

print("\nt4")
t4 = type4(start,end,G,ts,te)
print(t4)

print("\nt4 gurobi")
t4g = g.type4(start,end,G,ts,te)
print(t4g)





