class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maximum = 0
        for sentence in sentences:
            words = sentence.count(' ') + 1
            maximum = max(maximum, words)
        return maximum        
