class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        required = Counter(
            ch.lower()
            for ch in licensePlate
            if ch.isalpha()
        )
        answer = ""
        for word in words:
            count = Counter(word)
            if all(count[ch] >= freq for ch, freq in required.items()):
                if not answer or len(word) < len(answer):
                    answer = word
        return answer
