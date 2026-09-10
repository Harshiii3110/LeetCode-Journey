class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        current = []
        def backtrack(start, remaining):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                # Skip duplicate choices at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Since array is sorted
                if candidates[i] > remaining:
                    break
                current.append(candidates[i])
                # Move to i + 1 because each number can be used once
                backtrack(i + 1, remaining - candidates[i])
                current.pop()
        backtrack(0, target)
        return result
