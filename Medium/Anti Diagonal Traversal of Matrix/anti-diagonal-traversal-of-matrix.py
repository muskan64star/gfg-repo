#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
        row = col = 0
        solution  = []
        while col < c and row < r:
            i = col
            j = row
            while i>=0 and j < n:
                solution.append(matrix[j][i])
                i -= 1
                j += 1
            if col < c - 1:
                col += 1
            else:
                row +=1
        return solution
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends