from collections import defaultdict
t=int(input())
n,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(t):
    i=0
    j=0
    mp=defaultdict(int)
    count=0
    while(j<n):
        mp[arr[j]]+=1
        if(len(mp)==(m+1)):
            #m multiply all elemtn in the map
            ans=1
            for k in mp:
                ans=ans*mp[k]
            count+=ans
        while len(mp)!=(m):
            mp[arr[i]]-=1
            if(mp[arr[i]]==0):
                del mp[arr[i]]
            i+=1
        # if(len(mp)==(m+1)):
        #     #m multiply all elemtn in the map
        #     ans=1
        #     for k in mp:
        #         ans=ans*mp[k]
        #     count+=ans
        j+=1
        
    print(count)
                
            