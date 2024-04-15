#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        size = max(max(a),max(b))
        memo = [0]*(size+1)
        ans = []
        for i in range(n):
            memo[b[i]] +=1
        
        for i in range(1,size+1):
            memo[i] += memo[i-1]
        for i in range(q):
            ans.append(memo[a[query[i]]])
        return ans
        # ans = []
        # i = 0
        # j = 0
        # count = 0
        # while i<n and j<q:
        #     k = a[query[j]]
        #     if b[i]<=k:
        #         count+=1
        #     i+=1
        #     if i==n:
        #         ans.append(count)
        #         i = 0
        #         count = 0
        #         j += 1
        ## for i in query:
        #     k = a[i]
        #     count = 0
        #     for num in b:
        #         if num<=k:
        #             count+=1
        ##     ans.append(count)
            
        # return ans 
                    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends