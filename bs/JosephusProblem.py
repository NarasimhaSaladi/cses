from collections import deque
def solve():
    n = int(input())
    # queue=deque(range(1,8))
    # ans=[]
    # while queue:
    #     element=queue.popleft()
    #     queue.append(element)
    #     ans.append(queue.popleft())
    # print(ans)
    arr=[i for i in range(1,n+1)]
    ind=0
    ans=[]
    while len(arr)!=0:
            ind=(ind+1)%len(arr)
            ans.append(arr.pop((ind)))
            
    print(ans)
if __name__ == "__main__":
    solve()