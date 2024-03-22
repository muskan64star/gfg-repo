#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		maxcount = 0
		ans = 0 
		for i in range(n):
		    arr1 = arr[i] 
		    a = arr1.count(1)
		    if a>maxcount:
		        maxcount = a
		        ans = i
		        
	    if maxcount>0:
	        return ans
	    else:
	        return -1
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends