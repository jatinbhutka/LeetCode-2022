'''
Parition an array into different contiguous subarrays such that the sum of the differences between the largest and smallest element in each subarray is maximum.
Note: No limit on number of subarrays you can create
How would you solve this? I started with a brute force recursive approach and added some memoization, it worked but was TLE for some cases.

Eg:
The array[ 10, 6, 1, 3 ] can be partitoned into [ 10, 6, 1] and [3]
10 - 1 + 3-3 = 9
'''

def getValue(arr, N):
    dp = [0 for i in range(N)]
    for i in range(1, N):
        # Stores the maximum and
        # minimum elements upto
        # the i-th index
        minn = arr[i]
        maxx = arr[i]
         
        j = i
         
        # Traverse the range [0, i]
        while(j >= 0):
           
            # Update the minimum
            minn = min(arr[j], minn)
    
            # Update the maximum
            maxx = max(arr[j], maxx)
    
            # Update dp[i]
            dp[i] = max(dp[i], maxx - minn + (dp[j - 1] if (j >= 1) else 0))
            j -= 1
    return dp[N-1]

a = [ 10, 6, 1, 3 ]
N = len(a)
print(getValue(a,N))




# Write a program to implement pow(a,b) without loops

# Mapper function:
def test(a):
    return a*a

m = [2,3,4]
y = map(test, m)
print(list(y))


# Lambda Function:
x = lambda a,b : a**b
print(x(2,4))



# Binary Search in Array:

#  Write a program to implement binary search.

def search(arr, n, start, end):
    if end >= start:
    
        mid = start + (end-start)//2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            return search(arr, n, start, mid-1)
        else:
            return search(arr, n, mid + 1, end)
    return "not prsent"


arr = [1,3,4,7,9,10, 12, 13, 15, 20]
print(search(arr, 15, 0, len(arr)-1))

# Time: O(Log N)





# Merge Sort:

def merge_sort(A):
    l = len(A)
    if l<2:
        return A
    else:
        mid = l//2
        
        left = A[:mid]
#        print("left", left)
        
        right = A[mid:]
#        print("right", right)
        
        merge_sort(left)
        merge_sort(right)
        
        merge(left, right, A)
    return A


def merge(left, right, A ):
    nl = len(left)
    nr= len(right)
    i=0 
    """ for left"""
    
    j=0 
    """ for right"""
    
    k=0 
    """ for main A"""
    
    while(i<nl and j<nr):
        if left[i]<=right[j]:
            A[k]=left[i]
            i+=1
        else:
            A[k]=right[j]
            j+=1
        k+=1
    while i < nl:
        A[k]=left[i]
        i+=1
        k+=1
    while j<nr:
        A[k]=right[j]
        j+=1
        k+=1
    return A

def main():
    A = [64, 25, 12, 22, 11]  
    print("Array to be sorted are:\n", A, "\n")
    
    A = merge_sort(A)
    print ("Merge Sorted array") 
    print(A)
