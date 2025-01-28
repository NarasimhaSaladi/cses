import bisect


def bisecl(arr, x, low):
    # Find the lower bound for x in arr[low:]
    # i want core function
    # return the index of the first element in arr[low:] that is >= x
    #dont use bisect module
    high=len(arr)-1
    n=len(arr)
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= x:
            n = mid  # Update lower bound index
            high = mid - 1  # Continue searching in the left half
        else:
            low = mid + 1  # Continue searching in the right half
    return low

def bisecr(arr,x,low):
    # Find the upper bound for x in arr[low:]
    # i want core function
    # return the index of the first element in arr[low:] that is > x
    #dont use bisect module
    high = n - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return low


def count_interesting_pairs(n, x, y, arr):
    total_sum = sum(arr)
    arr.sort()
    count = 0
    
    for i in range(n):
        # Calculate the valid sum range for arr[i]
        low = total_sum - y - arr[i]
        high = total_sum - x - arr[i]
        
        # Find the lower bound for valid j (where arr[j] >= low)
        low_ind = bisecl(arr, low, i+1)
        
        # Find the upper bound for valid j (where arr[j] <= high)
        high_ind = bisecr(arr, high, i+1) - 1
        
        if low_ind <= high_ind:
            count += (high_ind - low_ind + 1)
    
    return count

# Read input
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Get the number of interesting pairs for the test case
    print(count_interesting_pairs(n, x, y, arr))
