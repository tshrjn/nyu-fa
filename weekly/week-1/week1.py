# ------------------------------------------------------------------
# Lecture Code
# ------------------------------------------------------------------
def insertion_sort(A):
    for j in range(1, len(A)):  # j is the number of cards we pick
        key = A[j]
        i =  j - 1              # we assume that A[0...j-1] is sorted and find place for A[j]
        while i > 0  and A[i] > key:
            A[i+1] = A[i]       # so far we thought that key should be in i + 1 position
            i = i - 1           # but it's too small.
        A[i+1] = key


# ------------------------------------------------------------------
# HW Code
# ------------------------------------------------------------------

# -----------
# HW- Q2 Code
# -----------

import random

def randomized_partition(A):
    x = random.choice(A) # pivot
    i = -1
    for j in range(len(A)):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i] # swap
    A[i+1], A[-1] = A[-1], A[i+1] # swap
    return i+1

def randomized_select(A, i):
    if len(A) == 1:
        return A[0]
    q = randomized_partition(A)
    k = q #+ 1
    if i == k: # pivot value is the answer
        return A[q]
    elif i < k:
        return randomized_select(A[:q], i)
    else:
        return randomized_select(A[q+1:], i-k)

def median1(A):
    return randomized_select(A, len(A)//2)

### Pythonic way
def select_nth(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)

def median2(items):
    return select_nth(len(items)//2, items)



# -----------
# HW- Q3 Code
# -----------
def solution(a,b):
    return min(a), max(b)