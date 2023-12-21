#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        pos = []
        neg = []
        ans = []
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        
        if len(pos)==n or len(neg)==n:
            return arr
        else:
            for i in range(min(len(pos), len(neg))):
                ans.append(pos[i])
                ans.append(neg[i])
        # Append remaining elements, if any
            for i in range(min(len(pos), len(neg)), len(pos)):
                ans.append(pos[i])

            for i in range(min(len(pos), len(neg)), len(neg)):
                ans.append(neg[i])
            arr[:] = ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends