#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		pre, curr, ans = 0, 0, 0
		for i in range(n):
		    curr = pre + arr[i]
		    pre = ans
		    ans = max(curr, ans)
	    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends