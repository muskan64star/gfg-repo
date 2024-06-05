class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum1 = sum(a)
        sum2 = sum(b)
        a = set(a)
        b = set(b)
        if sum1-sum2==0:
            return 1
        diff = abs(sum1-sum2)
        if diff & 1 == 1:
            return -1
        for i in a:
            if (diff-i) in b:
                return 1
                
        return -1

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends