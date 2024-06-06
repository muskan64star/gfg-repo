#User function Template for python3

def max_sum(a,n):
    #code heres
    # max_i = a.index(max(a))
    # ans = a[max_i]*(n-1)
    # i = max_i+1
    # j = 0
    # while j<n-1:
    #     if i>=n:
    #         i = 0
    #     ans += a[i]*j
    #     i+=1
    #     j+=1
    
    total_sum=sum(a)
    ans=0
    for i in range(n):
        ans+=(i*a[i])
    
    first_ele=a[0]
    last_ele=a[n-1]
    curr_sum=ans
    for i in range(1,n):
        curr_sum+=first_ele
        curr_sum-=(last_ele*(n-1))
        curr_sum+=(total_sum-(first_ele+last_ele))
        ans=max(curr_sum,ans)
        first_ele=last_ele
        last_ele=a[n-i-1]
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends