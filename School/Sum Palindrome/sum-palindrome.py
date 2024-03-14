#User function Template for python3

class Solution:
    def ispalindrome(self, n):
        a = str(n)
        if a==a[::-1]:
            return 1
        else:
            return -1
    def isSumPalindrome (self, n):
        # code here 
        for i in range(6):
            new = self.ispalindrome(n)
            if new==1:
                return n
            rev = int(str(n)[::-1])
            n = n+rev
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isSumPalindrome(n))
# } Driver Code Ends