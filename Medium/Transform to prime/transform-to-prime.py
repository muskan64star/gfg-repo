#User function Template for python3



class Solution:
    def minNumber(self, arr,n):
        def is_prime(n):
            if n==1:
                return False
            if n==2 or n==3:
                return True
            if n%2==0 or n%3==0:
                return False
            i=5
            while i*i<=n:
                if n%i==0 or n%(i+2)==0:
                    return False
                i+=6
            return True
        # code here
        total = sum(arr)
        j=total
        while not is_prime(total):
            total+=1
        return total-j


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends