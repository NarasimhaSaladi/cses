import heapq
from sortedcontainers import SortedList

def solve():
    x, n = map(int, input().split())
    arr = list(map(int, input().split()))

    def longest_passages(x, n, traffic_lights):
        max_heap = [-x]  # Start with the whole street as one segment
        positions = SortedList([0, x])  # Keep positions sorted

        for l in traffic_lights:
            positions.add(l)

            # Find left and right neighbors
            idx = positions.index(l)
            left, right = positions[idx - 1], positions[idx + 1]

            # Update the heap
            heapq.heappush(max_heap, -(l - left))
            heapq.heappush(max_heap, -(right - l))
            # heapq.heappush(max_heap, -(right - left))  # Old segment (lazy delete)

            # Remove invalid entries lazily
            heapq.heappop(max_heap)
            # Print the longest passage
            print(-max_heap[0])

    longest_passages(x, n, arr)

if __name__ == "__main__":
    solve()
