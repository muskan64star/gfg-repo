class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	dup = set()
    	seen = set()
    	
    	for item in arr:
    	    if item in seen:
    	        dup.add(item)
    	    else:
    	        seen.add(item)
    	        
        if len(dup)>0:
            return sorted(dup)
        else:
            return [-1]
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends