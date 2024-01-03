#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        zero = -1
        one = -1
        two = -1
        size = len(S) + 1
        
        for i in range(len(S)):
            if S[i] == '0':
                zero = i
            elif S[i] == '1':
                one = i
            elif S[i] == '2':
                two = i
            
            if zero != -1 and one != -1 and two != -1:
                tmp_size = max(zero, one, two) + 1 - min(zero, one, two)
                if tmp_size < size:
                    size = tmp_size
        
        if size == len(S) + 1:
            return -1
        else:
            return size

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends