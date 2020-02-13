class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.holder=[]
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.holder.append(word)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word in self.holder:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        n=len(prefix)
        for i in self.holder:
            if i[:n]==prefix:
                return True
        return False