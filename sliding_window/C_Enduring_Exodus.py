from bisect import bisect_left, bisect_right

n, k = map(int, input().split())
s = input()
arr = [i for i in range(n) if s[i] == '0']

def solve(mid):
    # Try each position as farmer location
    # for farmer_pos in range(len(arr)):
    #     farmer = arr[farmer_pos]
    #     # Find range where cows can be placed
    #     # (within mid distance from farmer)
    #     left = bisect_left(arr, farmer - mid)
    #     right = bisect_right(arr, farmer + mid)
        
    #     # Count available positions for cows
    #     count = right - left - 1  # -1 for farmer
        
    #     # If we can place k cows, solution exists
    #     if count >= k:
    #         return True
    # return False
    for farmer in arr:
        count=0
        left=bisect_left(arr,farmer-mid)
        right=bisect_right(arr,farmer+mid)
        count=right-left
        if(count>=(k+1)):
            return True
    return False

low, high = 0, arr[-1] - arr[0]
ans = high

while low <= high:
    mid = (low + high) // 2
    if solve(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
        
print(ans)