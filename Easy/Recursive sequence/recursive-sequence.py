#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        c = 1
        sumf = 0
        mod = 10**9+7
        for i in range(1,n+1):
            ans = 1
            for j in range(i):
                ans *= c
                c+=1
            sumf += ans
        return (sumf%mod)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends