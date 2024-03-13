# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        n = len(mat)
        sum_mat = [ [] for _ in range(n+n-1) ] 
        # print(sum_mat)
        
        for row in range(n):
            for col in range(n):
                sum_i = row + col
                
                sum_mat[sum_i].append(mat[row][col])
                # print(sum_mat)
                
        for i in range(len(sum_mat)):
            if i % 2 == 0:
                sum_mat[i] = sum_mat[i][::-1]
                
        res = []
        for i in sum_mat:
            res.extend(i)
                
        return res


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends