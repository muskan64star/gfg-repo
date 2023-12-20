#User function Template for python3

class Solution:
    def findWinner(self, n, A):
        res=0
        for i in A:
            res=res^i
        if (n&1==1 and res>0):
            return 2
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        A = input().split()
        for itr in range(n):
            A[itr] = int(A[itr])

        ob = Solution()
        print(ob.findWinner(n, A))

# } Driver Code Ends