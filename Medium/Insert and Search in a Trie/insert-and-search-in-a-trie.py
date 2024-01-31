#User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    # Function to insert a string into the Trie
    def insert(self, root, key):
        for i in range(len(key)):
            # Calculate the index of the current character in the children array
            index = ord(key[i]) - ord('a')

            # If the child node for the current character doesn't exist, create a new node
            if not root.children[index]:
                root.children[index] = TrieNode()

            # Move to the next level in the Trie
            root = root.children[index]

        # Mark the last node as the end of the inserted word
        root.isEndOfWord = True

    # Function to search for a string in the Trie
    def search(self, root, key):
        for i in range(len(key)):
            # Calculate the index of the current character in the children array
            index = ord(key[i]) - ord('a')

            # If the child node for the current character doesn't exist, the word is not present
            if not root.children[index]:
                return False

            # Move to the next level in the Trie
            root = root.children[index]

        # If the end of the word flag is true, the word is present in the Trie
        return root.isEndOfWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends