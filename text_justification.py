class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        n = len(words)
        i = 0

        while i < n:
            j = i
            line_length = 0

            # Find the maximum number of words that fit
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            line = ""

            # Last line or a line with only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - line_length
                gaps = num_words - 1
                spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces + (1 if k - i < extra_spaces else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result
