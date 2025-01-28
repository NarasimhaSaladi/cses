n,x=map(int,input().split())
s=input()
i=0
j=0
a=0
b=0
maxi=0
summ=0
while(j<n):
    if(s[j]=='a'):
        a+=1
    if(s[j]=='b'):
        b+=1
        summ+=a
    while(summ > x):
        if(s[i]=='a'):
            summ-=b
            a-=1
        if(s[i]=='b'):
            b-=1
        i+=1
    
    # if(summ<=x):
    maxi=max(maxi,j-i+1)
    j+=1
print(maxi)