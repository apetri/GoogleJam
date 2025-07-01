class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = dict()

class TrieRoot:
    root = TrieNode()

    def add(self,word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end_of_word = True
    
    def search(self,word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.end_of_word
