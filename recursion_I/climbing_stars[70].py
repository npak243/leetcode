class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def count_steps(n: int) -> int:
            if n <= 2:
                return n

            if cache.get(n):
                return cache.get(n)

            result = count_steps(n - 1) + count_steps(n - 2)
            cache[n] = result

            return result

        return count_steps(n)
