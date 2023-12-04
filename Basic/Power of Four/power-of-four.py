# you may use python module's
# just return true/false or 1/0
class Solution():
    def isPowerofFour(self, n):
         # code here
        if n>0 and n&(n-1)==0 and n&0XAAAAAAAA==0:
            return True
        else:
            False
#{ 
 # Driver Code Starts
# Your code goes here

if __name__=='__main__':
    test = int(input())
    for i in range(test):
        num = int(input())
        if(Solution().isPowerofFour(num)):
            print (1)
        else:
            print (0)
# } Driver Code Ends