from gurobipy import *

def contrainte(n,arcs):
    nbvar = len(arcs)
    ar = arcs[n]
    cont = [0]*nbvar
    cont[n] = 1
    for i in range(nbvar):
        if arcs[i].v == ar.u:
            cont[i] = -1
    if(sum(cont) == 1):
        return [0]*nbvar
    return cont

def pl(s_dep,s_arr,graph):
    sommets,arcs = graph
    nbvar = len(arcs)
    a = [[0]*nbvar, [0]*nbvar]

    print(a)
    for i in range(nbvar):
        ar = arcs[i]
        print(ar,s_dep,s_arr)
        if ar.u == s_dep:
            a[0][i] = -1
        if ar.v == s_arr:
            a[1][i] = -1
        print(ar)
        print(a)

    for i in range(nbvar):
        a += [contrainte(i,arcs)]

    nbcont = len(a)
    b = [-1,-1] + [0]*(nbcont-2)
    c = [1]*nbvar
    return a,b,c

def type4(s_dep,s_arr,graph):
    a,b,c = pl(s_dep,s_arr,graph)
    print("\na:",a)
    print("\nb:",b)
    print("\nc:",c)

    nbcont = len(a)
    nbvar = len(a[0])

    lignes = range(nbcont)
    colonnes = range(nbvar)

    m = Model("mogplex")

    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.INTEGER, lb=0, name="x%d" % (i+1)))

    m.update()

    obj = LinExpr();
    obj = 0
    for j in colonnes:
        obj += c[j] * x[j]

    m.setObjective(obj,GRB.MINIMIZE)

    for i in lignes:
        m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)

    m.optimize()

    print("")
    print('Solution optimale:')
    for j in colonnes:
        print('x%d'%(j+1), '=', x[j].x)
    print("")
    print('Valeur de la fonction objectif :', m.objVal)

    sommets,arcs = graph
    res = []
    for i in colonnes:
        if(x[i].x == 1):
            res += [arcs[i]]

    return res
