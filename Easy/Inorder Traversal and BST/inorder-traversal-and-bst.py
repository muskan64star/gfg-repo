#User function Template for python3

import math
class Solution:
    def isRepresentingBST(self, arr, N):
            if N == 1:
                return 1
            mid_index = N//2
            left = arr[0:mid_index]
            if N == 2:
                right = [math.inf]
            else:
                right = arr[mid_index+1:]
            for i in left:
                if i > arr[mid_index]:
                    return 0
            for j in right:
                if j < arr[mid_index]:
                    return 0
            return int(self.isRepresentingBST(left, len(left)) and self.isRepresentingBST(right, len(right)))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends