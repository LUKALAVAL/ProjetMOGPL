from math import inf

def transformT2(start, end, G, ts, te):
    '''
    Transforms G into G_ for type2 path
    '''
    ### Initialisation
    sommets,arcs = G
    G_ = {}
    Vin = {}
    Vout = {}
    t_tot = 0
    for s in sommets:
        Vin[s] = []
        Vout[s] = []

    ### Create V
    for a in arcs:
        t_tot += a.t
        Vout[a.u] += [(a.u,a.t)]
        Vin[a.v] += [(a.v,a.t+a.l)]
    for s in sommets:
        Vout[s] = list(set(Vout[s]))
        Vin[s] = list(set(Vin[s]))
    V = {k: Vin.get(k, 0) + Vout.get(k, 0) for k in set(Vin)}

    ### Create G_
    for k,v in V.items():
        v.sort()
        length = len(v)
        if(k == start):
            # invert arrows directions : for example (A,i) -0-> (A,i+1) in a normal transformation, but here we want (A,i) -MAX*i-> (A,i-1) to force dijkstra to find the desired path
            v.reverse()
            for i in range(length):
                if(v[i][1] >= ts):
                    if(i+1 < length and v[i+1][1] >= ts):
                        G_[v[i]] = {v[i+1] : (t_tot+1)*(i+1)}
                    else:
                        G_[v[i]] = {}
                        break
        elif(k == end):
            for i in range(length):
                if(v[i][1] <= te):
                    if(i+1 < length and v[i+1][1] <= te):
                        G_[v[i]] = {v[i+1] : 0}
                    else:
                        G_[v[i]] = {}
                        break
        else:
            for i in range(length-1):
                G_[v[i]] = {v[i+1] : 0}
            G_[v[length-1]] = {}

    for a in arcs:
        condition = (a.u == start and a.t >= ts) or (a.v == end and a.t+a.l <= te) or (a.u != start and a.v != end)
        if condition:
            if (a.u,a.t) in G_.keys():
                G_[(a.u,a.t)][(a.v,a.t+a.l)] = a.l
            else:
                G_[(a.u,a.t)] = {(a.v,a.t+a.l) : a.l}

    return G_

def transformT3(start,end,G,ts,te):
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
    for k,v in V.items():
        v.sort()
        length = len(v)
        if(k == start):
            for i in range(length):
                if(v[i][1] >= ts):
                    if(i+1 < length and v[i+1][1] >= ts):
                        G_[v[i]] = {v[i+1] : 0}
                    else:
                        G_[v[i]] = {}
                        break
        elif(k == end):
            for i in range(length):
                if(v[i][1] <= te):
                    if(i+1 < length and v[i+1][1] <= te):
                        G_[v[i]] = {v[i+1] : 0}
                    else:
                        G_[v[i]] = {}
                        break
        else:
            for i in range(length-1):
                G_[v[i]] = {v[i+1] : v[i+1][1]-v[i][1]}
            G_[v[length-1]] = {}

    for a in arcs:
        condition = (a.u == start and a.t >= ts) or (a.v == end and a.t+a.l <= te) or (a.u != start and a.v != end)
        if condition:
            if (a.u,a.t) in G_.keys():
                G_[(a.u,a.t)][(a.v,a.t+a.l)] = a.l
            else:
                G_[(a.u,a.t)] = {(a.v,a.t+a.l) : a.l}
    return G_

def transformT4(start,end,G,ts,te):
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
    for k,v in V.items():
        v.sort()
        length = len(v)
        if(k == start):
            for i in range(length):
                if(v[i][1] >= ts):
                    if(i+1 < length and v[i+1][1] >= ts):
                        G_[v[i]] = {v[i+1] : 0}
                    else:
                        G_[v[i]] = {}
                        break
        elif(k == end):
            for i in range(length):
                if(v[i][1] <= te):
                    if(i+1 < length and v[i+1][1] <= te):
                        G_[v[i]] = {v[i+1] : 0}
                    else:
                        G_[v[i]] = {}
                        break
        else:
            for i in range(length-1):
                G_[v[i]] = {v[i+1] : 0}
            G_[v[length-1]] = {}

    for a in arcs:
        condition = (a.u == start and a.t >= ts) or (a.v == end and a.t+a.l <= te) or (a.u != start and a.v != end)
        if condition:
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

def type1(start,end,G,ts,te):
    '''
    Returns the shortest path (type1) from start to end
    '''
    ### Transform G into G_
    G_ = transformT4(start,end,G,ts,te)

    ### Initialisation
    # s_dep correspond au couple (sommet,t) où t a la plus petite valeur possible
    s_dep = (start,inf)
    for k in G_.keys():
        if k[0] == start and k[1] < s_dep[1]:
            s_dep = k

    if s_dep[1] == inf:
        return []

    paths = dijkstra(s_dep,G_)

    ### Explicit the shortest path
    # On récupère le chemin qui arrive au plus tot au sommet end
    path = []
    val = inf
    for s_arr,ch in paths.items():
        if s_arr[0] == end and s_arr[1] < val:
            path = ch[1]
            val = s_arr[1]

    return dijk_to_path(path)

def type2(start,end,G,ts,te):
    '''
    Returns the shortest path (type2) from start to end
    '''
    ### Transform G into G_ for type2 path
    G_ = transformT2(start,end,G,ts,te)

    ### Initialisation
    # s_dep correspond au couple (sommet,t) où t a la plus grande valeur possible
    s_dep = (start,-1)
    for k in G_.keys():
        if k[0] == start and k[1] > s_dep[1]:
            s_dep = k

    if s_dep[1] == -1:
        return []

    ### Shortest path algorithm
    paths = dijkstra(s_dep,G_)

    ### Explicit the shortest path
    # On récupère le chemin qui arrive au plus tard au sommet end
    path = []
    val = -1
    for s_arr,ch in paths.items():
        if s_arr[0] == end and s_arr[1] > val:
            path = ch[1]
            val = s_arr[1]

    # lors de la conversion du chemin, c'est le sommet sommet de départ au plus tard réalisable qui est conservé
    return dijk_to_path(path)

def type3(start,end,G,ts,te):
    '''
    Returns the shortest path (type3) from start to end
    '''
    ### Transform G into G_
    G_ = transformT3(start,end,G,ts,te)

    ### Initialisation
    s_dep = (start,inf)
    for k in G_.keys():
        if k[0] == start and k[1] < s_dep[1]:
            s_dep = k

    if s_dep[1] == inf:
        return []

    ### Shortest path algorithm
    paths = dijkstra(s_dep,G_)

    ### Excplicit the shortest path
    path = []
    val = inf
    for s_arr,ch in paths.items():
        if s_arr[0] == end and ch[0] < val:
            path = ch[1]
            val = ch[0]

    return dijk_to_path(path)
    pass

def type4(start,end,G,ts,te):
    '''
    Returns the shortest path (type4) from start to end
    '''
    ### Transform G into G_
    G_ = transformT4(start,end,G,ts,te)

    ### Initialisation
    s_dep = (start,inf)
    for k in G_.keys():
        if k[0] == start and k[1] < s_dep[1]:
            s_dep = k

    if s_dep[1] == inf:
        return []

    ### Shortest path algorithm
    paths = dijkstra(s_dep,G_)

    ### Excplicit the shortest path
    path = []
    val = inf
    for s_arr,ch in paths.items():
        if s_arr[0] == end and ch[0] < val:
            path = ch[1]
            val = ch[0]

    return dijk_to_path(path)
