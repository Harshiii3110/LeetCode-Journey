class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = {}

        def solve(expr):
            if expr in memo:
                return memo[expr]

            results = []

            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i + 1:])

                    for left in left_results:
                        for right in right_results:
                            if ch == '+':
                                results.append(left + right)
                            elif ch == '-':
                                results.append(left - right)
                            else:
                                results.append(left * right)

            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return solve(expression)
