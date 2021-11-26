from math import inf

def transform(G):
    '''
    Transforms G into G_
    '''
    ### Initialisation
    sommets,arcs = G
    G_ = {}
    Vin = {}
    Vout = {}
    for s in sommets:
        Vin[s] = []
        Vout[s] = []

    ### Create V
    for a in arcs:
        Vout[a.u] += [(a.u,a.t)]
        Vin[a.v] += [(a.v,a.t+a.l)]
    for s in sommets:
        Vout[s] = list(set(Vout[s]))
        Vin[s] = list(set(Vin[s]))
    V = {k: Vin.get(k, 0) + Vout.get(k, 0) for k in set(Vin)}

    ### Create G_
    for v in V.values():
        v.sort()
        length = len(v)
        for i in range(length-1):
            G_[v[i]] = {v[i+1] : 0}
        G_[v[length-1]] = {}

    for a in arcs:
        if (a.u,a.t) in G_.keys():
            G_[(a.u,a.t)][(a.v,a.t+a.l)] = a.l
        else:
            G_[(a.u,a.t)] = {(a.v,a.t+a.l) : a.l}

    return G_



def dijkstra(s_dep,graph):
    '''
    Finds the shortest path from s_dep to every other points
    '''
    s_kw = { s_dep : [0,[s_dep]] }
    s_unkw = { s : [inf,None] for s in graph if s != s_dep }

    for s in graph[s_dep]:
        s_unkw[s] = [graph[s_dep][s],s_dep]

    while s_unkw and any(s_unkw[s][0] < inf for s in s_unkw):
        s = min(s_unkw,key=s_unkw.get)
        val_s, prev_s = s_unkw[s]
        for t in graph[s]:
            if t in s_unkw:
                new_val = val_s + graph[s][t]
                if new_val < s_unkw[t][0]:
                    s_unkw[t] = [new_val,s]

        s_kw[s] = [val_s,s_kw[prev_s][1] + [s]]
        del s_unkw[s]

    return s_kw

def dijk_to_path(dijk_path):
    '''
    Convert a path given from Dijkstra into a "normal" path
    '''
    dijk_path.reverse()
    path = [(None,None)]
    for c in dijk_path:
        if c[0] != path[-1][0]:
            path += [c]
    path.reverse()
    return path[:-1]

def type1(graph):
    pass

def type2():
    pass

def type3():
    pass

def type4(s_start,s_finish,G):
    '''
    Returns the shortest path (type4) from s_start to s_finish
    '''
    ### Transform G into G_
    G_ = transform(G)

    ### Initialisation
    s_dep = (s_start,inf)
    for k in G_.keys():
        if k[0] == s_start and k[1] < s_dep[1]:
            s_dep = k

    if s_dep[1] == inf:
        return []

    ### Shortest path algorithm
    paths = dijkstra(s_dep,G_)

    ### Return the shortest path
    path = []
    val = inf
    for s_arr,ch in paths.items():
        if s_arr[0] == s_finish and ch[0] < val:
            path = ch[1]
            val = ch[0]

    return dijk_to_path(path)
