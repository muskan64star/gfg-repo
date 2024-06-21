#User function Template for python3


class Solution:
    def compareFrac (self, s):
        
        n1, n2 = s.split()
        frac1 = n1.index("/")
        frac2 = n2.index("/")
        a1 = int(n1[:frac1])
        a2 = int(n1[frac1+1:-1])
        b1 = int(n2[:frac2])
        b2 = int(n2[frac2+1:])
        
        if a1/a2==b1/b2:
            return "equal"
        elif a1/a2 > b1/b2:
            return n1[:-1]
        else:
            return n2
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends