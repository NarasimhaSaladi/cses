a,b=map(int,input().split())

lis=list(map(int,input().split()))

def solve():
    low=min(lis)
    high=max(lis)*b
    def func(mid):
        total=0
        for i in range(a):
            total+=mid//lis[i]
        return total
            
            
    while(low<=high):
        mid=(low+high)>>1
        if(func(mid)>=b):
            high=mid-1
        else:
            low=mid+1
    return low
if __name__=='__main__':
    print(solve())


