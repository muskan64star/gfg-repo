#User function Template for python3

class Solution:

    def CountPS(self, S, N):
        # code here
        c = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if S[i]==S[j]:
                    a = S[i:j+1]
                    if a == a[::-1]:
                        c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.CountPS(S,N))
# } Driver Code Ends