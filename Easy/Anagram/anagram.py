#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        dict1 = {}
        for i in a:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in b:
            if j in dict1:
                dict1[j]-=1
            else:
                return False
        
        for k in dict1.keys():
            if dict1[k]!=0:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends