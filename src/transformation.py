def transform(graph):
    sommets,arcs = graph
    Vin = {}
    Vout = {}
    for s in sommets:
        Vin[s] = []
        Vout[s] = []
    for a in arcs:
        Vout[a.u] += [(a.u,a.t)]
        Vin[a.v] += [(a.v,a.t+a.l)]
    for s in sommets:
        Vout[s] = list(set(Vout[s]))
        Vin[s] = list(set(Vin[s]))
    V = {k: Vin.get(k, 0) + Vout.get(k, 0) for k in set(Vin)}

    A = {}
    for v in V.values():
        v.sort()
        length = len(v)
        for i in range(length-1):
            A[v[i]] = {v[i+1] : 0}
        A[v[length-1]] = {}

    for a in arcs:
        if (a.u,a.t) in A.keys():
            A[(a.u,a.t)][(a.v,a.t+a.l)] = a.l
        else:
            A[(a.u,a.t)] = {(a.v,a.t+a.l) : a.l}

    return A
