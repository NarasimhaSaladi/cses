n,r=map(int,input().split())
lis=list(map(int,input().split()))
i=0
j=0
dist=0
ways=0
while(j<n):
    while abs(lis[j]-lis[i]) >  r:
        ways+=(n-j)
        i+=1
    j+=1
print(ways)