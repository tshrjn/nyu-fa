# ------------------------------------------------------------------
# Lecture Code
# ------------------------------------------------------------------
def quick_sort(A, start=0, end=None):
    if end is None:
        end = len(A) - 1

    if start < end:
        q = randomized_partition(A, start, end)
        quick_sort(A,start,q-1)
        quick_sort(A,q+1,end)


import random
def randomized_partition(A, p, r):
    idx = random.randint(p,r) # randomised pivot 
    A[r], A[idx] = A[idx], A[r]
    x = A[r]                    # last element as pivot
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i] # swap
    A[i+1], A[r] = A[r], A[i+1] # swap
    return i+1

# def randomized_partition(A):
#     x = random.choice(A) # pivot
#     i = -1
#     for j in range(len(A)):
#         if A[j] <= x:
#             i = i+1
#             A[i], A[j] = A[j], A[i] # swap
#     A[i+1], A[-1] = A[-1], A[i+1] # swap
#     return i+1


def binary_search(A, x, lo=0, hi=None):
    if hi is None:
        hi = len(A)-1

    if lo > hi:
        return None

    mid = (lo+hi)//2
    if x == A[mid]:
        return mid
    elif x < A[mid]:
        return binary_search(A, x , lo, mid-1)
    else:
        return binary_search(A, x , mid+1, hi)





# ------------------------------------------------------------------
# HW Code
# ------------------------------------------------------------------


# -----------
# HW- Q2b Code
# -----------

def findMin(A, l=0, r=len(A)-1):
    if r < l:
        return A[0]
    if r == l:
        return A[l]

    # python3 division else use int typecasting 
    m = int((l + r)/2)
 
    if m < r and A[m+1] < A[m]:
        return A[m+1]
    if m > l and A[m] < A[m - 1]:
        return A[m]
    if A[r] > A[m]:
        return findMin(A, l, m-1)
    return findMin(A, m+1, r)

# -----------
# HW- Q3 Code
# -----------

def localMinUtil(arr, low, high):
    n = len(arr)
    # python3 division else use int typecasting 
    mid = low + (high-low)//2
     
    if ((mid == 0 or arr[mid-1] > arr[mid]) 
    and (mid == n-1 or arr[mid] < arr[mid+1])):
        return mid
     
    elif(mid > 0 and arr[mid-1] < arr[mid]):
        return localMinUtil(arr, low, mid-1)
     
    return localMinUtil(arr, mid+1, high)
 
def localMin(arr):
    return arr[localMinUtil(arr, 0, len(arr)-1)]     

# -----------
# HW- Q4 Code
# -----------

def findMaximum(arr, low, high): 
   if (low == high):
     return arr[low]
   if ((high == low + 1) and arr[low] >= arr[high]):
      return arr[low]
 
   if ((high == low + 1) and arr[low] < arr[high]):
      return arr[high]
      
   # python3 division else use int typecasting  
   mid = (low + high)//2
 
   if ( arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]):
      return arr[mid]
 
   if (arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]):
     return findMaximum(arr, low, mid-1)
   else: 
     return findMaximum(arr, mid + 1, high)
