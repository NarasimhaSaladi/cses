# def binary_search_left(arr, target, predicate):
#     """
#     Custom binary search to find the leftmost index where predicate(arr[mid], target) is True.
#     """
#     low, high = 0, len(arr) - 1
#     result = len(arr)  # Default to an index out of bounds if no valid index is found
#     while low <= high:
#         mid = (low + high) // 2
#         if predicate(arr[mid], target):
#             result = mid  # Store potential result
#             high = mid - 1  # Narrow search range to the left
#         else:
#             low = mid + 1  # Narrow search range to the right
#     return result

# # Define the predicate function
# def predicate(item, target):
#     return item[0] >= target

# # Input: number of elements and the threshold difference
# n, d = map(int, input().split())
# ans = []

# # Read input and store values in 'ans'
# for _ in range(n):
#     m, f = map(int, input().split())
#     ans.append((m, f))

# # Sort the array based on the first element of each tuple (m values)
# ans.sort()

# cost = 0
# maxi = 0
# prefix_sum = [0] * (n + 1)

# # Compute prefix sum for faster sum calculation
# for idx in range(n):
#     prefix_sum[idx + 1] = prefix_sum[idx] + ans[idx][1]

# # Iterate over each element as the right boundary
# for j in range(n):
#     # Use custom binary search with the predicate function
#     target = ans[j][0] - d + 1
#     i = binary_search_left(ans, target, predicate)
    
#     # Calculate the sum of values in the range [i, j] using prefix sums
#     cost = prefix_sum[j + 1] - prefix_sum[i]
    
#     # Update the maximum cost
#     maxi = max(maxi, cost)

# print(maxi)
n, d = map(int, input().split())
friends = [list(map(int, input().split())) for _ in  range(n)]
friends.sort(key=lambda x: x[0])

left = right = ans = sum = 0

while right < n:
    sum += friends[right][1]
    
    while friends[right][0] >= friends[left][0] + d:
        sum -= friends[left][1]
        left += 1
    
    ans = max(ans, sum)
    right += 1

print(ans)