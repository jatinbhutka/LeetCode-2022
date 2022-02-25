Parition an array into different contiguous subarrays such that the sum of the differences between the largest and smallest element in each subarray is maximum.

Note: No limit on number of subarrays you can create

How would you solve this? I started with a brute force recursive approach and added some memoization, it worked but was TLE for some cases.

Eg:

The array[ 10, 6, 1, 3 ] can be partitoned into [ 10, 6, 1] and [3]
10 - 1 + 3-3 = 9


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
