class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        current = []
        def backtrack(index, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                # Same candidate can be reused
                backtrack(i, remaining - candidates[i])
                current.pop()
        backtrack(0, target)
        return result
