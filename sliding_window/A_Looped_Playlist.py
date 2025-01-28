n, p = map(int, input().split())
arr = list(map(int, input().split()))

# Double the array to handle wrap-around cases
arr = arr + arr
total = sum(arr[:n])  # Sum of original array

if p <= total:
    # Case 1: Normal sliding window
    i = 0  # Window start
    j = 0  # Window end
    curr_sum = 0
    min_len = float('inf')
    start = 0
    
    while j < 2*n:
        curr_sum += arr[j]
        while curr_sum >= p and i <= j:
            if j - i + 1 < min_len:
                min_len = j - i + 1
                start = i % n
            curr_sum -= arr[i]
            i += 1
        j += 1
    print(start + 1, min_len)

else:
    # Case 2: When p > total
    complete_cycles = p // total
    remaining = p % total
    
    if remaining == 0:
        print(1, n * complete_cycles)
    else:
        # Find the maximum element and its position
        # This ensures we continue from the best possible position
        max_val = max(arr[:n])
        max_pos = arr[:n].index(max_val)
        
        # Start our search from the max element position
        curr_sum = 0
        min_extra = n  # Initialize to maximum possible length
        start_pos = max_pos
        
        # Try starting from the max element
        j = max_pos
        count = 0
        while count < n and curr_sum < remaining:
            curr_sum += arr[j]
            count += 1
            j = (j + 1) % n
            
        if curr_sum >= remaining and count < min_extra:
            min_extra = count
            start_pos = max_pos
            
        print(start_pos + 1, n * complete_cycles + min_extra)