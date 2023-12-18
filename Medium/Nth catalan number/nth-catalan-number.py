
class Solution:
    def findCatalan(self, n : int) -> int:
        # code here
        f=1
        for i in range(n):
           f=(f*2*(2*i+1))//(i+2)
        
        return f%1000000007
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.findCatalan(n)
        
        print(res)
        

# } Driver Code Ends