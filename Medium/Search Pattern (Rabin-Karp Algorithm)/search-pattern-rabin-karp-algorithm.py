#User function Template for python3

class Solution:
    def search(self, pattern, text):
        # code here
        n,m=len(text),len(pattern)
        if n<m:
            return -1
        else:
            a=[]
            for i in range(0,n):
                if text[i:i+m]==pattern:
                    a+=[1+i]
            return a
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends