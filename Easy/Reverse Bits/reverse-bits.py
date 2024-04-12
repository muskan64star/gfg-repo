#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        num = bin(x)[2:]
        n = len(num)
        j = 32-n
        ans = 0
        for i in range(n):
            ans += int(num[i])*(2**j)
            j+=1
            
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends