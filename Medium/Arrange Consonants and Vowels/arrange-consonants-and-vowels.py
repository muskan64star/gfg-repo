#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        v_arr = ["a", "e", "i", "o", "u"]
        dummy_vowel = Node(None)
        dummy_conso = Node(None)
        vowel = dummy_vowel
        conso = dummy_conso
        if head==None:
            return head
        curr = head
        while curr:
            if curr.data in v_arr:
                vowel.next = curr
                vowel = vowel.next
            else:
                conso.next = curr
                conso = conso.next
            curr = curr.next
        
        vowel.next = dummy_conso.next
        conso.next = None
        return dummy_vowel.next

#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends