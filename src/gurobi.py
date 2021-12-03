from gurobipy import *

def contrainte(n,arcs):
    nbvar = len(arcs)
    ar = arcs[n]
    cont = [0]*nbvar
    nb_pred = 0
    for i in range(nbvar):
        ar2 = arcs[i]
        if (ar2.v == ar.u):
            nb_pred += 1
            if(ar2.t + ar2.l <= ar.t):
                cont[i] = -1
    if(nb_pred != 0):
        cont[n] = 1
    return cont

def matrice_contraite(start,end,G,ts,te):
    sommets,arcs = G
    nbvar = len(arcs)
    a = [[0]*nbvar, [0]*nbvar]

    for i in range(nbvar):
        ar = arcs[i]
        if ar.u == start:
            if ar.t >= ts:
                a[0][i] = -1
            else:
                # force the variable to be set to 0
                line = [0]*nbvar
                line[i] = 1
                a += [line]
        if ar.v == end:
            if ar.t+ar.l <= te:
                a[1][i] = -1
            else:
                # force the variable to be set to 0
                line = [0]*nbvar
                line[i] = 1
                a += [line]

    for i in range(nbvar):
        a += [contrainte(i,arcs)]

    return a

def pl(start,end,G,ts,te):
    a = matrice_contraite(start,end,G,ts,te)
    nbcont = len(a)
    b = [-1,-1] + [0]*(nbcont-2)
    sommets,arcs = G
    c = []
    for arc in G[1]:
        c += [arc.l]
    return a,b,c

def type4(start,end,G,ts,te):
    # avoid gurobi output messages
    env = Env(empty=True)
    env.setParam('OutputFlag', 0)
    env.start()

    a,b,c = pl(start,end,G,ts,te)
    # print("\na:")
    # for l in a:
    #     print(l)
    # print("\nb:",b)
    # print("\nc:",c)

    nbcont = len(a)
    nbvar = len(a[0])

    lignes = range(nbcont)
    colonnes = range(nbvar)

    m = Model("mogplex",env=env)

    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.BINARY, lb=0, name="x%d" % (i+1)))

    m.update()

    obj = LinExpr();
    obj = 0
    for j in colonnes:
        obj += c[j] * x[j]

    m.setObjective(obj,GRB.MINIMIZE)

    for i in lignes:
        m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)

    m.optimize()

    # print("")
    # print('Solution optimale:')
    # for j in colonnes:
    #     print('x%d'%(j+1), '=', x[j].x)
    # print("")
    # print('Valeur de la fonction objectif :', m.objVal)

    # return empty path if the model has no solution
    try:
        m.objVal
    except:
        return []

    sommets,arcs = G
    res = []
    for i in colonnes:
        if(x[i].x == 1):
            res += [arcs[i]]

    return res
