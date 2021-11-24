from Arc import Arc

def str_to_arc(arc_str):
    u,v,t,l = "","","",""
    i = 1
    while arc_str[i] != ',':
        u += arc_str[i]
        i += 1
    i += 1
    while arc_str[i] != ',':
        v += arc_str[i]
        i += 1
    i += 1
    while arc_str[i] != ',':
        t += arc_str[i]
        i += 1
    i += 1
    while arc_str[i] != ')':
        l += arc_str[i]
        i += 1
    return Arc(u,v,int(t),int(l))

def interp_file(path):
    f = open(path,'r')
    n = int(f.readline())
    m = int(f.readline())
    sommets = []
    arcs = []
    for i in range(n):
        sommets += [f.readline()[:-1]]
    for i in range(m):
        arcs += [str_to_arc(f.readline())]
    f.close()
    return sommets, arcs

def interp_input():
    sommets = []
    arcs = []
    n = int(input("Nombre de sommets (int) : "))
    m = int(input("Nombre d'arcs (int) : "))
    for i in range(n):
        s = input("Nom du sommet " + str(i) + " : ")
        sommets += [s]
    for i in range(m):
        a = input("Arc " + str(i) + " (u,v,t,lambda) : ")
        arcs += [str_to_arc(a)]
    return sommets, arcs

def check_graph(sommets, arcs):
    if len(sommets) != len(set(sommets)):
        return False
    for a in arcs:
        if not (a.u in sommets) or not (a.v in sommets):
            return False
    return True
