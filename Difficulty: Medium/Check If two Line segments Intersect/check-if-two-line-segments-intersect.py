#User function Template for python3

class Solution:
    def direction(self, p, q, r):

        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        if val == 0:

            return 0

        return 1 if val > 0 else -1

    def onSegment(self, p, q, r):

        return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])

    def doIntersect(self, p1, q1, p2, q2):

        d1 = self.direction(p1, q1, p2)

        d2 = self.direction(p1, q1, q2)

        d3 = self.direction(p2, q2, p1)

        d4 = self.direction(p2, q2, q1)

        if d1 != d2 and d3 != d4:

            return "true"

        if d1 == 0 and self.onSegment(p1, p2, q1):

            return "true"

        if d2 == 0 and self.onSegment(p1, q2, q1):

           return "true"

        if d3 == 0 and self.onSegment(p2, p1, q2):

            return "true"

        if d4 == 0 and self.onSegment(p2, q1, q2):

            return "true"

        return "false"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)

# } Driver Code Ends