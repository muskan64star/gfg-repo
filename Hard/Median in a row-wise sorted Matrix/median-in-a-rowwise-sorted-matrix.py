#User function Template for python3

import bisect
class Solution:
    def median(self, matrix, R, C):
        _min = float("inf")
        _max = float("-inf")

        for i in range(R):
            _min = min(matrix[i][0], _min)
            _max = max(matrix[i][C - 1], _max)

        medianPos = (R * C + 1) // 2

        while _min < _max:
            mid = _min + (_max - _min) // 2
            midPos = 0

            for i in range(R):
                pos = bisect.bisect(matrix[i], mid)
                midPos += pos

            if midPos < medianPos:
                _min = mid + 1
            else:
                _max = mid

        return _min



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends