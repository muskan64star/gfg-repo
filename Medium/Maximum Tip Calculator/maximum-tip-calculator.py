
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        diff = []
        for i in range(n):
            diff.append((abs(arr[i]-brr[i]), i))
        tip = 0
        diff.sort(reverse=True)
        for i in range(n):
            ind = diff[i][1]
            if (arr[ind]>brr[ind] or y<=0) and x>0:
                tip += arr[ind]
                x -= 1
            else:
                tip += brr[ind]
                y -= 1
        return tip



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends