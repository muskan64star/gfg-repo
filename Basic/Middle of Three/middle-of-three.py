#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        #code here
        max1 = max(A,B,C)
        min1 = min(A,B,C)
        
        if A!=max1 and A!=min1:
            return A
        if B!=max1 and B!=min1:
            return B
        else:
            return C



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends