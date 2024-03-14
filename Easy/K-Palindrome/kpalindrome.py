#User function Template for python3
from collections import Counter
class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        # d = Counter(str)
        # odd = 0
        # for key,value in d.items():
        #     if value%2!=0:
        #         odd+=1
        # odd -= k
        # if odd>1:
        #     return 0
        # else:
        #     return 1
        
        i = 0
        j = n-1
        while i<j:
            if str[i]!=str[j]:
                if k==0:
                    return 0
                k-=1
                if str[i]==str[j-1]:
                    j-=1
                    continue
                else:
                    i+=1
                    continue
            i+=1
            j-=1
        return 1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        n = int(arr[0])
        k = int(arr[1])
        str = input()
        
        ob = Solution()
        print(ob.kPalindrome(str, n, k))
# } Driver Code Ends