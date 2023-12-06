
class Solution:
    def nthFibonacci(self, n : int) -> int:
        # code here
        if n==1 or n==2:
            return 1
        a = 1
        b = 1
        while n>2:
            c = (a+b)%(1e9+7)
            a = b
            b = c
            n-=1
        
        return int(c)
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends