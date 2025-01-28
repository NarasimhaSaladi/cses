from collections import deque
def solve():
    x,n= map(int,input().split())
    arr=list(map(int,input().split()))
    max_heap=[-x]
    import heapq

    # Function to calculate the longest passage
    def longest_passages(x, n, traffic_lights):
        positions=[0,8]
        # positions.add(0)
        # positions.add(8)
        
        for l in traffic_lights:
            positions.append(l)
            print(positions)
            s_positions=sorted(positions)
            print(s_positions)
            
            ind=s_positions.index(l)

            left=s_positions[ind-1]
            right=s_positions[ind+1]
            heapq.heappush(max_heap,-(l-left))
            heapq.heappush(max_heap,-(right-l))
            max_heap.remove(-(right-left))
            heapq.heapify(max_heap)
            
            
            print(max_heap[0])
            
            
            
            
    longest_passages(x,n,arr)

        
if __name__ == "__main__":
    solve()