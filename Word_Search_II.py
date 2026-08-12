class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        # Build Trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word
        rows = len(board)
        cols = len(board[0])
        result = []
        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word is not None:
                result.append(nxt.word)
                nxt.word = None
            board[r][c] = '#'
            if r > 0 and board[r - 1][c] != '#':
                dfs(r - 1, c, nxt)
            if r + 1 < rows and board[r + 1][c] != '#':
                dfs(r + 1, c, nxt)
            if c > 0 and board[r][c - 1] != '#':
                dfs(r, c - 1, nxt)
            if c + 1 < cols and board[r][c + 1] != '#':
                dfs(r, c + 1, nxt)
            board[r][c] = ch
            # Remove unused Trie branch for optimization
            if not nxt.children and nxt.word is None:
                del node.children[ch]
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, root)
        return result        
