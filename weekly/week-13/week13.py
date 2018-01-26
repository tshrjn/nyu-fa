# Q1a

def mst_via_bfs(graph, start):
    queue = [start]
    mst = {start:[]}

    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in mst.keys():    
                queue.append(neighbour)

                insert_edge(mst, (node, neighbour))
                insert_edge(mst, (neighbour, node))

    return mst

def insert_edge(graph, edge):
    u, v = edge

    if graph.get(u):
        graph[u].append(v)
    else:
        graph[u] = [v]

# Q1b

def mst_via_bfs2(graph, start):
    e = find_unique_edge(graph)
    queue = [start]
    mst = {start:[]}
    count = 1

    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in mst.keys() and neighbour not in e:    
                queue.append(neighbour)

                insert_edge(mst, (node, neighbour))
                insert_edge(mst, (neighbour, node))
                count += 1

    # can it also be implemented (w/o count) as len(mst) != len(G)?
    if count != len(G): 
        return mst_via_bfs(graph, start) # from Q1a

    return mst

def insert_edge(graph, edge):
    u, v = edge

    if graph.get(u):
        graph[u].append(v)
    else:
        graph[u] = [v]

def find_unique_edge(graph):
    # weights is a dictionary on edges (tuple)
    from collections import Counter
    c = Counter(weights.values())

    for k,v in c.items():
        if v == 2: # since undirected => 2 edges
            unique = k
            break
    
    for k,v in weights.items():   
        if unique == v:
            return k


# Q2

def mst_prim_modified(graph, start, weights ):
    n = len(graph)
    key = [sys.maxsize]*(n)
    p = [None]*(n)

    key[start] = 0

    import heapq

    q = heapq.heapify(G.v)

    while q:
        q_prime = lowest_bucket_with_root(q)
        u = heapq.heappop(q_prime)
        for v in G[u]:
            if v in q and weights[(u, v)] < key[v]:
                p[v] = u
                key[v] = weights[(u, v)]

#Q3

p = {}
rank = {}

def make_set(x):
    p[x] = x
    rank[x] = 0

def union(x,y):
    px, py = find_set(x), find_set(y) 

    if rank[px] > rank[py]:
        p[yp] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x]) # path-compression
    return p[x]



# Q4
s & t & x & y & z\\
$\infty$ & $\infty$ & $\infty$ & $\infty$ & 0\\
2 & $\infty$ & 7 & $\infty$ & 0\\
2 & 5 & 7 & 9 & 0\\
2 & 5 & 6 & 9 & 0\\
2 & 4 & 6 & 9 & 0\\

s & t & x & y & z\\
NIL & NIL & NIL & NIL & NIL\\
z & NIL & z & NIL & NIL\\
z & x & z & s & NIL\\
z & x & y & s & NIL\\
z & x & y & s & NIL\\

s & t & x & y & z\\
0 & $\infty$ & $\infty$ & $\infty$ & $\infty$\\
0 & 6 & $\infty$ & 7 & $\infty$\\
0 & 6 & 4 & 7 & 2\\
0 & 2 & 4 & 7 & 2\\
0 & 2 & 4 & 7 & -2\\

s & t & x & y & z\\
NIL & NIL & NIL & NIL & NIL\\
NIL & s & NIL & s & NIL\\
NIL & s & y & s & t\\
NIL & x & y & s & t\\
NIL & x & y & s & t\\