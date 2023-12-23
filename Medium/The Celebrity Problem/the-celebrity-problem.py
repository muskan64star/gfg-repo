#User function Template for python3

class Solution:
    def celebrity(self, a, n):
        i, j = 0, n - 1

        while i < j:
            if a[i][j] == 1:
                i += 1
            else:
                j -= 1

        for x in range(n):
            if x != i and (a[i][x] == 1 or a[x][i] == 0):
                return -1

        return i
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends