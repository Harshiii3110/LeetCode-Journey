class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_map = {}
        for i, word in enumerate(list1):
            index_map[word] = i
        min_sum = float('inf')
        answer = []
        for j, word in enumerate(list2):
            if word in index_map:
                current_sum = index_map[word] + j
                if current_sum < min_sum:
                    min_sum = current_sum
                    answer = [word]
                elif current_sum == min_sum:
                    answer.append(word)
        return answer
