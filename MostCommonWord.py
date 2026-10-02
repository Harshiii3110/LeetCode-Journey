class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        words = []
        word = ""
        for ch in paragraph.lower():
            if ch.isalpha():
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)
        count = {}
        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1
        return max(count, key=count.get)
