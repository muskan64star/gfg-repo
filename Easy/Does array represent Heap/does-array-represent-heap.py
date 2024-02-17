
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here            
        i = 0
        while i<n:
            jump = i+1
            if n<=jump+i:
                return 1
            else:
                if jump+i+1<n:
                    if arr[i]<arr[jump+i] or arr[i]<arr[jump+i+1]:
                        return 0
                else:
                    if arr[i]<arr[jump+i]:
                        return 0
            i+=1


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends