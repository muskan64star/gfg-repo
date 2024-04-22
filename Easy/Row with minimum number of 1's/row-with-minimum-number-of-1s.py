#User function Template for python3

class Solution:
    def minRow(self,n,m,a):
        #code here
        one = m
        ans = 1
        for i in range(n):
            if a[i].count(1)<one:
                one = a[i].count(1)
                ans = i+1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        A=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            A.append(B)
        ob=Solution()
        print(ob.minRow(N,M,A))
# } Driver Code Ends