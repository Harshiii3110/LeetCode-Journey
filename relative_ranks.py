class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n= len(score)
        athletes = [(score[i], i) for i in range(n)]
        athletes.sort(reverse=True)
        answer = [""] * n
        for rank, (sc, index) in enumerate(athletes, 1):
            if rank == 1:
                answer[index] = "Gold Medal"
            elif rank == 2:
                answer[index] = "Silver Medal"
            elif rank == 3:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank)
        return answer
