
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        close = arr[0]
        s = 0
        e = n-1
        while s<=e:
            m = (s+e)//2
            if (abs(arr[m]-k) < abs(close-k)) or (abs(arr[m]-k)==abs(close-k) and arr[m]>close):
                close = arr[m]
            if arr[m]<k:
                s = m+1
            elif arr[m]>k:
                e = m-1
            else:
                return arr[m]
        return close



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends