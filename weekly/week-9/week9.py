def greedy_activity_selector(s,f,a):
    n = len(s)
    A = set(a[0])
    k = 1 # index of last activity in A
    for m in range(1,n):
        if s[m] >= f[k]:
            A.add(a[m])
            k=m
    return A


def Huffman(C):
    n = count(C) # |C| 
    Q = C # Q is a min-heap-priority queue according to freq)
    for i in range(n-1):
        allocate new node z
        z.left = x = Extract_min(Q)
        z.right = y = Extract_min(Q)
        z.freq = x.freq + y.freq
        Insert(Q,z)
    return Extract_min(Q)




# ------------------------------------------------------------------
# HW8 Code
# ------------------------------------------------------------------



# -----------
# HW- Q1c Code
# -----------

def maxRevenue(r):
    n = len(r)
    if n < 3:
        return max(r)
        
    DP = [0]*(n+1)
    DP[1] = r[0]

    for i in range(2,n+1):
        DP[i] = max(DP[i - 1], DP[i - 2] + r[i-1])

    return DP[n]

# -----------
# HW- Q1d Code
# -----------

def check(i,j,x):
    return int(x[i-1] - x[j-1] >= k)

def maxRevenue(r,x):
    DP = [0]*(n+1)
    DP[1] = r[0]

    for i in range(2,n+1):
        for j in range(1,i-1):
            temp = DP[j] + check(i,j,x)*DP[i]
            if temp > DP[i]:
                DP[i] = temp 
        DP[i] = max(DP[i], r[i-1])

    return DP[n]


# -----------
# HW- Q2b Code
# -----------

def maxProfit(E,W,C):
    n = len(E)
    DP_E = [0]*n
    DP_W = [0]*n
    DP_E[0] = E[0]
    DP_W[0] = W[0]

    for i in range(1,n):
        DP_E[i] = max(DP_E[i-1] + E[i], DP_W[i-1] + E[i] - C )
        DP_W[i] = max(DP_W[i-1] + W[i], DP_E[i-1] + W[i] - C )

    return max(DP_E[n-1], DP_W[n-1])


# -----------
# HW- Q4b Code
# -----------

def minStops(stops, m):
    count = 0
    maxreach, idx = 0, 0

    while maxreach + m < stops[-1]:
        j = 0
        while stops[j] - maxreach <= m:
            j += 1
        idx = j-1
        maxreach = stops[idx]
        count += 1
    return count

# -----------
# HW- Q5 Code
# -----------


class TVShow():
    def __init__(self,s,f):
        self.s = s
        self.f = f

def minTVShows(shows, s, f):
    sorted_shows = sorted(shows, key= lambda x: x.s)

    curr = TVShow(s,s)
    curr_s = s
    ans = set()

    for show in sorted_shows:
        if show.s <= curr_s:
            print("if")
            if show.f > curr.f:
                print("ifif")
                curr = show
        else:
            print("else")
            ans.add(curr)
            curr = TVShow(curr.f, curr.f)
            curr_s = curr.s   

    return ans

def minTVShows(shows, s, f):
    sorted_shows = sorted(shows, key= lambda x: x.s)

    curr = TVShow(s,s)
    curr_s = s
    ans = set()

    i = 0
    while i < len(sorted_shows):
        if sorted_shows[i].s <= curr_s:
            flag = True
            if sorted_shows[i].f > curr.f:
                curr = sorted_shows[i]
            i += 1
        else:
            flag = False
            ans.add(curr)
            curr = (curr.f, curr.f)
            curr_s = curr.s  

    if flag:
        ans.add(curr)    
    return ans

#  while skip
def minTVShows(shows, s, f):
    sorted_shows = sorted(shows, key= lambda x: x[0])

    curr = (s,s)
    curr_s = s
    ans = set()

    i = 0
    while i < len(sorted_shows):
        print("i", curr, sorted_shows[i], curr_s, ans)
        if sorted_shows[i][0] <= curr_s:
            flag = True
            if sorted_shows[i][1] > curr[1]:
                print("ifif")
                curr = sorted_shows[i]
            i += 1
        else:
            flag = False
            print("else")
            ans.add(curr)
            curr = (curr[1], curr[1])
            curr_s = curr[0]  

    if flag:
        ans.add(curr)    
    return ans
