n,x=map(int,input().split())
w=list(map(int,input().split()))
c=list(map(int,input().split()))

i=0
j=0
wei=0
cost=0
maxi=-1e9
while j<n:
    wei+=w[j]
    cost+=c[j]
    while(wei>x):
        cost-=c[i]
        wei-=w[i]
        i+=1
    maxi=max(maxi,cost)    
    j+=1
print(maxi)
        
    