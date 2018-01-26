def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
 
    # Create a character array to store the lcs string
    lcs = [""] * (index+1)
    lcs[index] = "\0"
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    print "LCS of " + X + " and " + Y + " is " + "".join(lcs) 


def lcs_length(X,Y):
    m, n = len(X), len(Y)
    C = [ [0]*(n+1) for _ in range(m+1) ]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1]+1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

INT_MIN = -32767
def bottom_up_cut_rod(p,n):
    r = [0]*(n+1)
    for j in range(1,n+1):
        max_val = INT_MIN
        for i in range(j):
             max_val = max(max_val, p[i] + r[j-i-1])
        r[i] = max_val
    
    return r[n]


# Dynamic Programming Python implementation of Matrix
# Chain Multiplication. See the Cormen book for details
# of the following algorithm
import sys
 
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]
 
    # m[i,j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]
 
    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0
 
    # L is chain length.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):
 
                # q = cost/scalar multiplications
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
 
    return m[1][n-1]
 
# Driver program to test above function
arr = [1, 2, 3 ,4]
size = len(arr)
 
print("Minimum number of multiplications is " +
       str(MatrixChainOrder(arr, size)))
# This Code is contributed by Bhavya Jain


# ------------------------------------------------------------------
# HW7 Code
# ------------------------------------------------------------------

# -----------
# HW- Q1 Code
# -----------

# -----------
# HW- Q2a Code
# -----------


def height(node):
    if node is None:
        return 0
    else:
        max_height = max([height(child) for child in node.children])
        node.height = max_height + 1
        return node.height


# -----------
# HW- Q2b Code
# -----------

memo = {}
def get_longest(from_node, to_node):
    if (from_node,to_node) in memo:
        return memo[(from_node,to_node)]
    if from_node == to_node:
        memo[(from_node,to_node)] = 0
        return memo[(from_node,to_node)]
    best = 0
    for from_node2, weight in G[from_node]:#.edges:
        best = max(best, get_longest(from_node2, from_node) + weight)
    memo[to_node] = best
    return best

# -----------
# HW- Q3 Code
# -----------

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(n+1)] for x in range(m+1)]
 
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    index = L[m][n]
 
    lcs = [""] * (index)
 
    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
 
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    return "".join(lcs)

def lps(s):
    return lcs(s, s[::-1])


def Sij(A):
    S = [[0 for x in range(n)] for x in range(n)]
    for i in range(n):
        S[i][i] = A[i]
        for j in range(i+1, n):
            S[i][j] = A[i][j-1] + A[j]

    return S

def max_Sij(A):
    n = len(A)
    L = [0] *(n)

    for i in range(2, n):
        L[i] = max(A[i], A[i] + L[i-1])

    return max(L)

def max_Sij(A):
    n = len(A)
    bestmax, total_max, bestmin = 1
    for i in range(n):
        if A[i]> 0:
            bestmax = bestmax * A[i]
            bestmin = bestmin * A[i]
        elif A[i] == 0:
            bestmax = bestmin = 1
        else:
            bestmax, bestmin = max(bestmin*A[i], 1), bestmax * A[i]

        total_max = max(total_max,bestmax)

    return total_max

    L = [0] *(n)
    
    for i in range(2, n):
        L[i] = max(A[i], A[i] + L[i-1])

    return max(L)








def SCS(X,Y):
    m , n = len(X), len(Y)
    print(X, m , len(X))
    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        M[i][0] = i
    for j in range(n+1):
        M[0][j] = j

    print(M)
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                M[i][j] = 1 + M[i-1][j-1]
            else:
                M[i][j] = 1 + max(M[i][j-1], M[i-1][j])

    return M[m-1][n-1], M





& 0& 1& 2& 3& 4& 5& 6& 7& 8& 9& 10& 11\\
& 1& 2& 2& 4& 5& 6& 7& 8& 9& 9& 11& 12\\
& 2& 2& 3& 5& 5& 7& 7& 9& 9& 10& 12& 12\\
& 3& 4& 5& 4& 6& 8& 9& 10& 11& 12& 11& 13\\
& 4& 5& 6& 6& 7& 9& 10& 11& 12& 13& 13& 14\\
& 5& 5& 7& 8& 7& 10& 10& 12& 12& 14& 15& 14\\
& 6& 7& 8& 9& 10& 8& 11& 13& 14& 15& 16& 17\\
& 7& 8& 9& 10& 11& 12& 13& 14& 15& 16& 17& 18\\
& 8& 9& 10& 11& 12& 13& 14& 14& 16& 17& 18& 19\\
& 9& 9& 11& 12& 12& 14& 14& 15& 15& 18& 19& 19\\


0& 0& 1& 2& 3& 4& 5& 6& 7& 8& 9& 10& 11\\
B& 1& 2& 2& 3& 4& 5& 6& 7& 8& 9& 10& 11\\
A& 2& 2& 3& 4& 4& 5& 6& 7& 8& 9& 10& 11\\
R& 3& 3& 4& 4& 5& 6& 7& 8& 9& 10& 10& 11\\
R& 4& 4& 5& 5& 6& 7& 8& 9& 10& 11& 11& 12\\
A& 5& 5& 6& 6& 6& 7& 8& 9& 10& 11& 12& 12\\
C& 6& 6& 7& 7& 7& 7& 8& 9& 10& 11& 12& 13\\
U& 7& 7& 8& 8& 8& 8& 9& 10& 11& 12& 13& 14\\
D& 8& 8& 9& 9& 9& 9& 10& 10& 11& 12& 13& 14\\
A& 9& 9& 10& 10& 10& 10& 10& 11& 11& 12& 13& 14\\


def SCS(X,Y):
    m, n = len(X), len(Y)
    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                M[i][j] = j
            elif j ==0:
                M[i][j] = i
            elif X[i-1] == Y[j-1]:
                M[i][j] = 1 + M[i-1][j-1]
            else:
                M[i][j] = 1 + min(M[i][j-1], M[i-1][j])

    return M[m][n]


def SCS_with_print(X,Y): # Row left
    m, n = len(X), len(Y)
    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                M[i][j] = j
            elif j ==0:
                M[i][j] = i
            elif X[i-1] == Y[j-1]:
                M[i][j] = 1 + M[i-1][j-1]
            else:
                M[i][j] = 1 + min(M[i][j-1], M[i-1][j])

    index = M[m][n]
 
    lcs = [""] * (index)
 
    i, j = m, n
    while i >= 0 and j >= 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1

        elif M[i-1][j] < M[i][j-1]:
            lcs[index-1] = X[i-1]
            index-=1
            i-=1
        else:
            lcs[index-1] = Y[j-1]
            index-=1
            j-=1
        

    return M[m][n], M, "".join(lcs), lcs

def SCS_with_print(X,Y): # Col up
    m, n = len(X), len(Y)
    M = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                M[i][j] = j
            elif j ==0:
                M[i][j] = i
            elif X[i-1] == Y[j-1]:
                M[i][j] = 1 + M[i-1][j-1]
            else:
                M[i][j] = 1 + min(M[i][j-1], M[i-1][j])

    index = M[m][n]
 
    lcs = [""] * (index)
 
    i, j = m, n
    while i >= 0 and j >= 0:
        if X[i-1] == Y[j-1]:
            print("equal: ",X[i-1],i,j)
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1

        elif M[i-1][j] > M[i][j-1]:
            print("greater M[i-1][j] > M[i][j-1]: ",Y[j-1],i,j)
            lcs[index-1] = Y[j-1]
            index-=1
            j-=1

        else:
            print("else: ", X[i-1],i,j)
            lcs[index-1] = X[i-1]
            index-=1
            i-=1
        

    return M[m][n], M, "".join(lcs), lcs
