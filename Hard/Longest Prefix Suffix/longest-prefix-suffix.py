#User function Template for python3

class Solution:
	def lps(self, s):
		# code here
		n = len(s)
        lps = [0] * n
        j,i= 0,1
        while i < n:
            if s[i] == s[j]:
                j+= 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps[n - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.lps(s)
		print(answer)

# } Driver Code Ends