#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		a = ""
		n = len(s)
		i = n-1
	    while i>=0:
	       if s[i]=="0":
	           a += "1"
	           break
	       else:
    	       a += "0"
    	       i -= 1
    	j = 0
    	while j<i:
    	    if s[j]=="1":
    	        break
    	    j += 1
	    if i==-1:
	        a = "1" + a[::-1]
	    else:
	        a = s[j:i] + a[::-1]
	    
	    return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends