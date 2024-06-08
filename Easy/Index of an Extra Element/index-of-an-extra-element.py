class Solution:
    def findExtra(self,n,a,b):
        #add code here
        s = 0
        e = n-2
        while s<=e:
            m = (s+e)//2
            if a[m]==b[m]:
                s = m+1
            else:
                e = m-1
        return s


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends