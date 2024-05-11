#User function Template for python3

class Solution:
    def jugglerSequence(self, n):
        # code here
        ans = [n]
        a = n
        while a!=1:
            if a%2==0:
                a = int(a**(1/2))
            else:
                a = int(a**(3/2))
            ans.append(a)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends