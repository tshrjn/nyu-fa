# ------------------------------------------------------------------
# Lecture Code
# ------------------------------------------------------------------

def merge(A,B):
    k = len(A)
    m = len(B)
    i, j = 0,0

    C = []

    while i < k and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
    if i == k:
        C += B[j:]
    else:
        C += A[i:]

    return C

def merge_sort(A):
    if len(A) > 1:
        m = len(A)//2
        l = merge_sort(A[:m])
        r = merge_sort(A[m:])
        return merge(l,r)
    else:
        return A

# ------------------------------------------------------------------
# HW Code
# ------------------------------------------------------------------


# -----------
# HW- Q2a Code
# -----------

def Eval(A, n, c):
    if n==0:
        return A[0]
    A[n-1] = A[n-1] + A[n]*c
    return Eval(A, n-1, c)

# -----------
# HW- Q2d Code
# -----------

def Eval2(A, n, c):
    if n==0:
        return A[0]
    
    return Eval2(A[:n/2+1], n/2, c) + c**(n/2)*Eval2(A[(n/2)+1:],n/2,c)


# -----------
# HW- Q2e Code
# -----------

def power(x, n):
    if n == 0:
        return 1
    if n%2 == 0:
        t = power(x,n/2)
        return t * t 
    else:
        return x * power(x, n-1)

# -----------
# HW- Q4 Code
# -----------

comparisons = 0
def min_max(A):
    global comparisons
    if len(A) == 1:
        return (A[0], A[0])
    if len(A) == 2:
        comparisons += 1
        if A[0] > A[1]:
            return (A[1],A[0])
        else:
            return (A[0],A[1])

    mid = len(A)//2
    mml = min_max(A[:mid])
    mmr = min_max(A[mid:])

    comparisons += 1
    if mml[0] > mmr[0]:
        _min = mmr[0]
    else:
        _min = mml[0]

    comparisons += 1
    if mml[1] < mmr[1]:
        _max = mmr[1]
    else:
        _max = mml[1]

    return (_min,_max)
