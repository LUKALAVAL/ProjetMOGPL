from math import inf

def dijkstra(s_dep,graph):
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
    path = [None]
    for c in dijk_path:
        s = c[0]
        if s != path[-1]:
            path += [s]
    return path[1:]

def type1(graph):
    pass

def type2():
    pass

def type3():
    pass

def type4(s_start,s_finish,graph):
    s_dep = (s_start,inf)
    for k in graph.keys():
        if k[0] == s_start and k[1] < s_dep[1]:
            s_dep = k

    if s_dep[1] == inf:
        return

    paths = dijkstra(s_dep,graph)
    path = []
    val = inf
    for s_arr,ch in paths.items():
        if s_arr[0] == s_finish and ch[0] < val:
            path = ch[1]
            val = ch[0]

    return dijk_to_path(path)
