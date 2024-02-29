#User function Template for python3
class Solution:

	
	def sumBitDifferences(self,arr, n):
    	# code here
    	ans=0
	    for i in range(32):
	        setBits=0
	        unsetBits=0
	        for num in arr:
	            if num &(1 << i):
	                setBits+=1
	            else:
	                unsetBits+=1
	        
	        ans+=setBits*unsetBits*2
	   
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
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends