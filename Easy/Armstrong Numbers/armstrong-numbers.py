#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        s = str(n)
        a, b, c = int(s[0]), int(s[1]), int(s[2])
        arms = a**3 + b**3 + c**3
        return "true" if n==arms else "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends