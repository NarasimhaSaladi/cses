from collections import defaultdict

n,m=map(int,input().split())

s1=input()
s2=input()

mp=defaultdict(int)
for i in range(m):
    mp[s2[i]]+=1

i=0
j=0
count=0
# print(mp)
while(j<n):

    mp[s1[j]]-=1
    while(mp[s1[j]]<0):
        mp[s1[i]]+=1
        i+=1
    count+=(j-i+1)
    # print(count)
    j+=1
print(count) 