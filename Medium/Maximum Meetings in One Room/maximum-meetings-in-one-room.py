from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        arr = []
        for i in range(N):
            arr.append([F[i], S[i], i+1])
        
        arr.sort()
        limit = arr[0][0]
        ans = [arr[0][2]]
        for i in range(1, len(arr)):
            if arr[i][1]>limit:
                ans.append(arr[i][2])
                limit = arr[i][0]
            else:
                continue
        ans.sort()
        return ans
        



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
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends