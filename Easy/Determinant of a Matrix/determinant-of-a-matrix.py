
#User function Template for python3

class Solution:
    
    #Function for finding determinant of matrix.
    def sub_mat(self,mat,r,c):
        n=len(mat)
        new_mat=[[0]*(n-1) for _ in range(n-1)]
        row,col=0,0
        for i in range(n):
            if i!=r:
                for j in range(n):
                    if j!=c:
                        new_mat[row][col]=mat[i][j]
                        col+=1
                col=0
                row+=1
        return new_mat

    def determinantOfMatrix(self,mat,n):
        if n==1:
            return mat[0][0]
        det=0
        for i in range(n):
            det+=((-1)**(1+i+1))*mat[0][i]*self.determinantOfMatrix(self.sub_mat(mat,0,i),n-1)
        return det

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends