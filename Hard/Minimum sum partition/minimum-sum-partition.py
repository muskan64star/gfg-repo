#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
	    def f(i, tar):
            dp = [False for i in range(tar + 1)]
            dp[0] = True
            if arr[0] <= tar:
                dp[arr[0]] = True
                for i in range(1, n):
                    cur = [False] * (tar + 1)
                    cur[0] = True
                    for k in range(1, tar + 1):
                        nt = dp[k]
                        t = False
                        if arr[i] <= k:
                            t = dp[k - arr[i]]
                        cur[k] = t or nt
                    dp = cur
                return dp
        tar = sum(arr)
        dp = f(n - 1, tar)
        mini = float('inf')
        for i in range(((tar + 1) // 2) + 1):
            if dp[i]:
                mini = min(mini, abs(i - (tar - i)))
        return mini


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends