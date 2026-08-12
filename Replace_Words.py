class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_root = False
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        root = TrieNode()
        # Build Trie
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_root = True
        def find_root(word):
            node = root
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    return word
                node = node.children[ch]
                prefix += ch
                # First root found is the shortest root
                if node.is_root:
                    return prefix
            return word
        words = sentence.split()
        for i in range(len(words)):
            words[i] = find_root(words[i])
        return " ".join(words)    
