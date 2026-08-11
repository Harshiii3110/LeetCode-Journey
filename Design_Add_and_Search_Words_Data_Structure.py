class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.end
            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], index + 1)
        return dfs(self.root, 0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
