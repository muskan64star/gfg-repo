#User function Template for python3

class Solution:
    def findMaxSum(self,n,m,mat):
        #code here
        if n<3 or m<3:
            return -1
        ans = 0
        for i in range(n-2):
            summ = 0
            for j in range(m-2):
                summ = mat[i][j]+mat[i][j+1]+mat[i][j+2]+mat[i+1][j+1]+mat[i+2][j]+mat[i+2][j+1]+mat[i+2][j+2]
                ans = max(ans, summ)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends