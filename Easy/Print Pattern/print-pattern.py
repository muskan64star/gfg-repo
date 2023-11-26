#User function Template for python3

class Solution:
    def pattern(self, N):
        # code here
        res = [N]
        t = N
        while N>0:
            N-=5
            res.append(N)
        while N<t:
            N+=5
            res.append(N)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends