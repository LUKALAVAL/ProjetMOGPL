from paths import *
import gurobi as g
from tests import performance
import matplotlib.pyplot as plt
from algo import algo
from interp import interp_file

ts = -1
te = 1000
tests_s = [('0','4',ts,te,'../graphs_s/g3.txt')
,('0','4',ts,te,'../graphs_s/g4.txt')
,('0','4',ts,te,'../graphs_s/g5.txt')
,('0','4',ts,te,'../graphs_s/g6.txt')
,('0','4',ts,te,'../graphs_s/g7.txt')
,('0','4',ts,te,'../graphs_s/g8.txt')
,('0','4',ts,te,'../graphs_s/g9.txt')
,('0','4',ts,te,'../graphs_s/g10.txt')
,('0','4',ts,te,'../graphs_s/g11.txt')
,('0','4',ts,te,'../graphs_s/g12.txt')
,('0','4',ts,te,'../graphs_s/g13.txt')
,('0','4',ts,te,'../graphs_s/g14.txt')
,('0','4',ts,te,'../graphs_s/g15.txt')
,('0','4',ts,te,'../graphs_s/g16.txt')
,('0','4',ts,te,'../graphs_s/g17.txt')
,('0','4',ts,te,'../graphs_s/g18.txt')
,('0','4',ts,te,'../graphs_s/g19.txt')
,('0','4',ts,te,'../graphs_s/g20.txt')
]

list_test = tests_s
symb = "--"

perfT1 = performance(type1,list_test)
perfT2 = performance(type2,list_test)
perfT3 = performance(type3,list_test)
perfT4 = performance(type4,list_test)
# perfG4 = performance(g.type4,list_test)
# perf_algo = performance(algo,list_test)

l_nb_sommets = [5,14,19,34,42,59,80,97,118,132,144,184,214,244,279,305,358,379]

plt.plot(l_nb_sommets,perfT1,symb)
plt.plot(l_nb_sommets,perfT2,symb)
plt.plot(l_nb_sommets,perfT3,symb)
plt.plot(l_nb_sommets,perfT4,symb)
# plt.plot(perfG4,l_nb_sommets,symb)
# plt.plot(perf_algo,symb)

plt.legend(["T1", "T2", "T3", "T4", "G4"])
# plt.legend(["T4", "G4"])

plt.show()

# G = interp_file("../graphs/test0.txt")
#
# p1,p2,p3,p4 = algo('0','20',G,0,20)
# pg = g.type4('0','20',G,0,20)
# print("p1 :",p1,"\n")
# print("p2 :",p2,"\n")
# print("p3 :",p3,"\n")
# print("p4 :",p4,"\n")
# print("pg :",pg,"\n")
