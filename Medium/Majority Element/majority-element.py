#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        dic = {}
        if len(A)==1:
            return A[0]
        for item in A:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        for i in A:
            if dic[i]>N//2:
                return i
        
        return -1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends