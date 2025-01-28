arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
def checksort(arr,ind):
    if(ind==n-1):
        return True
    if(arr[ind]>arr[ind+1]):
        return False
    return checksort(arr,ind+1)

res=checksort(arr,0)
print(res)