class Solution:
    def ExtractNumber(self,sentence):
        #code here
        li = list(sentence.split())
        ans = -1
        for item in li:
            if item[0].isdigit() and "9" not in item:
                    ans = max(ans, int(item))
                    
        return ans


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends