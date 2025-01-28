class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        ind=0
        while len(arr)>1:
            ind=(ind+k)%len(arr)
            arr.pop((ind))
            # print(arr)
        return arr[-1]
        


                