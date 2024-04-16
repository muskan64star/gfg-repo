#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        maxarea=0
        stack=[]
        for i in range(n+1):
            while stack and (i==n or histogram[stack[-1]]>histogram[i]):
                height=histogram[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=abs(i-stack[-1]-1)
                maxarea=max(maxarea,width*height)
            stack.append(i)
        return maxarea

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends