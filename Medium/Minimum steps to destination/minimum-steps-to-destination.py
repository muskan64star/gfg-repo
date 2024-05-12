#User function Template for python3

class Solution:
    def minSteps(self, d):
        # code here
        i = 1
        while i<2*d:
            if (((i*(i+1))//2) + d)%2 == 0 and ((i*(i+1))//2) >= d:
                return i
            i+=1
        # steps = 0
        # state = 0
        # i = 1
        # while state<d:
        #     if state+i<=d:
        #         state += i
        #         steps+=1
        #     else:
        #         state -= i
        #         steps+=1
        #     if state==d:
        #         return steps
        #     i+=1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends