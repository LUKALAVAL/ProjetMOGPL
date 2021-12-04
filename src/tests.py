from time import time
from interp import *

def measure(fun,test):
    start,end,ts,te,name = test
    G = interp_file(name)
    print(name)
    t = time()
    path = fun(start,end,G,ts,te)
    t = time() - t
    print(t)
    print(path)
    return t

def performance(fun,list_test):
    '''
    Calcul l'efficacite de la fonction fun sur une liste de tests
    Renvoie une liste des temps chronométrés
    '''
    perf = []
    for test in list_test:
        perf += [measure(fun,test)]
    return perf
