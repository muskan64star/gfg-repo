#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def divisorGame(self, n):
        #Code here
        i = 1
        a = 0
        while i<n and n>0:
            if n%i==0:
                n = n-i
                a = abs(a-1)
                
        return a==1
            

#{ 
 # Driver Code Starts.


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())

        obj = Solution()
        ans = obj.divisorGame(n)

        if ans:
            print("True")
        else:
            print("False")

        t -= 1
# } Driver Code Ends