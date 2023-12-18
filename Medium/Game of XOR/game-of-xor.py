#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        res = 0
        for i in range(N):
            if ((i + 1) & 1) and ((N - i) & 1):
                res = (res ^ A[i])
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.gameOfXor(N,A))
# } Driver Code Ends