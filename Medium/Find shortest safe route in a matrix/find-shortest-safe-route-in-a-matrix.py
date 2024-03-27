from typing import List

class Solution:
    def findShortestPath(self, mat : List[List[int]]) -> int:
        hth=len(mat)
        wth=len(mat[0])
        
        def ok(x,y):
            nonlocal mat,hth,wth
            if mat[y][x]==0:
                return False
            for dx,dy in [(0,1,),(0,-1,),(1,0,),(-1,0,)]:
                nx=x+dx
                ny=y+dy
                if 0<=nx<wth and 0<=ny<hth:
                    if mat[ny][nx]==0:
                        return False
            return True
        
        def dfs(x,y,py=-1):
            nonlocal mat,hth,wth
            if x==wth-1:
                return 1
            mn=float('inf')
            for dy in [1,-1]:
                ny=y+dy
                if 0<=ny<hth and ny!=py and ok(x,ny):
                    mn=min(mn,dfs(x,ny,y)+1)
            nx=x+1
            if 0<=nx<wth and ok(nx,y):
                mn=min(mn,dfs(nx,y)+1)
            return mn
        
        ans=[dfs(0,y) for y in range(hth) if ok(0,y)]
        ans=min(ans) if len(ans)>0 else -1
        
        return (ans if ans!=float('inf') else -1)



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        mat=IntMatrix().Input(a[0], a[1])
        
        obj = Solution()
        res = obj.findShortestPath(mat)
        
        print(res)
        

# } Driver Code Ends