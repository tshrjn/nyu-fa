# -----------
# HW- Q3a Code
# -----------
# undirected graph
G = {0: [1],
    1: [2],
    2: [1,3],
    3: [2]}

G = {0: [1],    
    1: [2,3],
    2: [1,3],
    3: [1,2]}


def DFSCheckCycle(G):
    n = len(G) # Number of vertices
    p = [None]*(n) #parent array
    
    color = ["white"]*(n)
    cycle = False

    for i in range(n):
        if color[i] == "white":
            p[i] = -1 # meaning it is a root of a DFS-tree of the DFS forest
            cycle = visit(i, G, color)
            if cycle:
                return cycle
    
    return False

def visit(u, G, color):
    cycle = False
    color[u] = "gray"
    for v in G[u]:
        if color[v] == "white":
            p[v] = u
            if visit(v, G, color):
                return True
        elif color[v] == "gray":
            cycle = True
            break
    color[u] = "black"# once DFS for this vertex ends, assign its color to black

    return cycle

# -----------
# HW- Q3b Code
# -----------

def DFSCheckCycle(G):
    n = len(G) # Number of vertices
    p = [None]*(n) #parent array
    
    color = ["white"]*(n)

    for i in range(n):
        if color[i] == "white":
            p[i] = -1 # meaning it is a root of a DFS-tree of the DFS forest
            visit(i, G, color)

def visit(u, G, color):
    cycle = False
    color[u] = "gray"
    for v in G[u]:
        if color[v] == "white":
            p[v] = u
            visit(v, G, color)
        elif color[v] == "gray":
            cycle = True
            break
    color[u] = "black"# // once DFS for this vertex ends, assign its color to black

    if cycle:
        printCycle(v,u)

def printCycle(v, u):
    print(u)
    u = p[u]

    while u != v:
        print(u)
        u = p[u]
    
# -----------
# HW- Q4a Code
# -----------

import sys
def BFS(G, s):
    for u in range(len(G)):
        if u == s:
            pass

    p = [None]*(n) #parent array
    color = ["white"]*(n)
    d = [sys.maxsize]*(n)

    color[s] = "gray"
    d[s] = 0
    
    q = []
    q.insert(0,s)

    while len(q):
        u = q[-1]
        del q[-1]

        for v in G[u]:
            if color[v] == "white":
                color[v] = "gray"
                d[v] += 1
                p[v] = u
                q.insert(0,s)

        color[u] = "black"
    return d

def politics(G, r, d):
    d1 = BFS(G, r)
    d2 = BFS(G, d)

    color = ["white"]*(n)

    for i in len(G):
        if d1[i] > d2[i] :
            color[i] = "red"
        elif d1[i] == d2[i] and d1[i] != sys.maxsize:
            color[i] = "red"
        elif d1[i] < d2[i]:
            color[i] = "blue"

# -----------
# HW- Q4b Code
# -----------

import sys
def BFS_mod(G, r, d):
    for u in range(len(G)):
        if u == s:
            pass

    p = [None]*(n) #parent array
    color = ["white"]*(n)
    d1 = [sys.maxsize]*(n)
    d2 = [sys.maxsize]*(n)

    color[r] = "red"
    color[d] = "blue"
    d1[r] = 0
    d2[d] = 0
    
    q = []
    q.insert(0,r)
    q.insert(0,d)

    while len(q):
        u = q[-1]
        del q[-1]

        for v in G[u]:
            if color[v] == "white":
                color[v] = color[u]
                d[v] += 1
                p[v] = u
                q.insert(0,s)




