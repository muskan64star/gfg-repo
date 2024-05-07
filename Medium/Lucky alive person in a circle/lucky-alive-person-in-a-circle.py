#User function Template for python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def find(self,N):
        # code here
        if N == 1:
            return 1
        # Calculate the luckiest person based on the formula
        return 2 * (N - 2 ** (N.bit_length() - 1)) + 1
        
        # head = tail = None
        # for i in range(1,N+1):
        #     newnode = Node(i)
        #     if head is None:
        #         head = newnode
        #         tail = newnode
        #     else:
        #         tail.next = newnode
        #         tail = newnode
        # tail.next = head
        # lucky = head
        # while lucky.next!=lucky:
        #     lucky.next = lucky.next.next
        #     lucky = lucky.next
        # return lucky.data

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.find(N))
# } Driver Code Ends