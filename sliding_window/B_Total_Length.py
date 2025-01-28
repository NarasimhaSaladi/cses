def solve(n, s, arr):
    total = 0  # sum of lengths of all good segments
    curr_sum = 0  # current segment sum    
    # For each ending position
    i=0
    j=0
    while j<n:
        curr_sum += arr[j]
        
        # While sum exceeds s, shrink the window
        while curr_sum > s:
            curr_sum -= arr[i]
            i += 1
            
        # If current segment is good, add its contribution
            # Add lengths of all valid segments ending at current right
        total += (j - i + 1)*((j-i+1)+1)//2
        j += 1
    
    return total


n,s=map(int,input().split())
arr=list(map(int,input().split()))
print(solve(n, s, arr))