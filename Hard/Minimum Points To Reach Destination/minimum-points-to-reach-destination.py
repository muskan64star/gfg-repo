#User function Template for python3
class Solution:
	def minPoints(self, m, n, points):
		# code here
		# Create a 2D DP table to store minimum points required to reach (m-1, n-1)
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the last cell
        dp[m - 1][n - 1] = max(1, 1 - points[m - 1][n - 1])
        
        # Fill the last column
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - points[i][n - 1])
        
        # Fill the last row
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - points[m - 1][j])
        
        # Fill the rest of the table
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # Minimum points required to reach (i, j) from either (i+1, j) or (i, j+1)
                min_points_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_points_on_exit - points[i][j])
        
        return dp[0][0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m,n = int(m),int(n)
		points = []
		for _ in range(m):
			temp = [int(x) for x in input().split()]
			points.append(temp)
		ob = Solution()
		ans = ob.minPoints(m,n,points)
		print(ans)




# } Driver Code Ends