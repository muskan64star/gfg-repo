#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        ans = ""
        while r>0:
            for i in range(min(len(s),n+2)):
                if s[i]=="0":
                    ans += "01"
                else:
                    ans += "10"
            s = ans
            ans = ""
            r -= 1
        return s[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends