def dfs_cc(G):
    color = ['white']*(len(G.Vertices))
    p = [None]*(len(G.Vertices))

    time = 0
    cc = 0
    for u in range(len(G.V)):
        if color[u] == 'white':
            cc += 1
            dfs_visit_cc(u,G, cc)

def dfs_visit_cc(u, G, cc):
    cc += 1
    ...
    ...
    ...

# Q1b
def dfs_dia(G):
    color = ['white']*(len(G.Vertices))
    p = [None]*(len(G.Vertices))

    time = 0
    for u in range(len(G.V)):
        if color[u] == 'white':
            dfs_visit_cc(u,G, 0)

def dfs_visit_dia(u, G, l):
    time += 1
    d[u] = time
    length[u] = l
    color[u] = 'grey'
    for v in G[u]:
        if color[v] == 'white':
            p[v] = u
            dfs_visit_dia(v, G, l+1)
    color[u] = 'black'
    time +=1
    f[u] = time

def diameter(G):
    dfs_dia(G)
    v = argmax(length)
    dfs_visit_dia(G, v, 0)
    D = max(length)

    return D
    ...
    ...
    ...



#  Q2
def dfs_visit_dia(u, G, A):
    time += 1
    d[u] = time
    A.append(u)
    color[u] = 'grey'
    for v in G[u]:
        if color[v] == 'white':
            p[v] = u
            dfs_visit_dia(v, G, l+1)
    color[u] = 'black'
    time +=1
    f[u] = time

    return A
