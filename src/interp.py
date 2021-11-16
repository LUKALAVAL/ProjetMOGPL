from Arc import Arc

def strToArc(arcStr):
    u,v,t,l = "","","",""
    i = 1
    while arcStr[i] != ',':
        u += arcStr[i]
        i += 1
    i += 1
    while arcStr[i] != ',':
        v += arcStr[i]
        i += 1
    i += 1
    while arcStr[i] != ',':
        t += arcStr[i]
        i += 1
    i += 1
    while arcStr[i] != ')':
        l += arcStr[i]
        i += 1
    return Arc(u,v,int(t),int(l))

def interpFile(f):
    n = int(f.readline())
    m = int(f.readline())
    listeSommets = []
    listeArcs = []
    for i in range(n):
        listeSommets += [f.readline()[:-1]]
    for i in range(m):
        listeArcs += [strToArc(f.readline())]
    return listeSommets, listeArcs

def interpInput():
    listeSommets = []
    listeArcs = []
    n = int(input("Nombre de sommets (int) : "))
    m = int(input("Nombre d'arcs (int) : "))
    for i in range(n):
        s = input("Nom du sommet " + str(i) + " : ")
        listeSommets += [s]
    for i in range(m):
        a = input("Arc " + str(i) + " (u,v,t,lambda) : ")
        listeArcs += [strToArc(a)]
    return listeSommets, listeArcs

def checkGraph(listeSommets, listeArcs):
    if len(listeSommets) != len(set(listeSommets)):
        return False
    for a in listeArcs:
        if not (a.u in listeSommets) or not (a.v in listeSommets):
            return False
    return True
