#User function Template for python3
class Solution:
    def stud(self, arr, N, p):
        s = 1
        pg = 0
        for i in range(N):
            if pg + arr[i] <= p:
                pg = pg + arr[i]
            else:
                s += 1
                pg = arr[i]
        return s

    def splitArray(self, arr, N, K):
        l = 0
        h = 0
        for i in range(N):
            h += arr[i]
            l = max(l, arr[i])

        while l <= h:
            m = l + (h - l) // 2
            num = self.stud(arr, N, m)
            if num > K:
                l = m + 1
            else:
                h = m - 1

        return l
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends