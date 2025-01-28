n,d = map(int, input().split())
ans = []
# Read input and store values in 'ans'
for i in range(n):
    m, f = map(int, input().split())
    ans.append((m, f))
    
ans.sort()
i=0
j=0
cost=0
maxi=0
while(j<n):
 
    cost+=ans[j][1]
    
    while((ans[j][0]-ans[i][0]) >= d ):
        cost-=ans[i][1]
        i+=1
    maxi=max(maxi,cost)
    j+=1
print(maxi)