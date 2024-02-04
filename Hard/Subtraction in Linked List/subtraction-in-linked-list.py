#User function Template for python3

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def subLinkedList(self, l1, l2): 
        # Code here
        # return head of difference list
        s1=''
        while l1:
            k=l1.data
            s1+=str(k)
            l1=l1.next
            
        s2=''
        while l2:
            a=l2.data
            s2+=str(a)
            l2=l2.next
        
        res=abs(int(s1)-int(s2))
        result_array = list(map(int, str(res)))
        result_head = Node(result_array[0])
        current = result_head

        for value in result_array[1:]:
            current.next = Node(value)
            current = current.next

        return result_head

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end='')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input() )
        LL1 = LinkedList()
        for i in arr1:
            LL1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input() )
        LL2 = LinkedList()
        for i in arr2:
            LL2.insert(i)
        
        ob = Solution()
        res = ob.subLinkedList(LL1.head, LL2.head)
        printList(res)
# } Driver Code Ends