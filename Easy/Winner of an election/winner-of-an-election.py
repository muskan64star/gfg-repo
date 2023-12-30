#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        di = {}
        ans = 0
        name = []
        for name in arr:
            if name in di:
                di[name]+=1
            else:
                di[name] = 1
        for keys in di:
            if di[keys]>ans or (di[keys] == ans and keys < name):
                ans = di[keys]
                name = keys
        return (name, ans)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends