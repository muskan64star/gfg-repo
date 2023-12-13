#User function Template for python3
class Solution:

	def countStrings(self, n):
        MOD = 10**9 + 7
        if n == 1:
            return 2
        first, second = 1, 2
        for i in range(2, n + 1):
            s = (first + second) % MOD
            first, second = second, s
        return second % MOD
#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends