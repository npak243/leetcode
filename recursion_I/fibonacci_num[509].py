class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        if n < 2:
            return n

        def fib_helper(num: int) -> int:
            if num < 2:
                return num
            if num in cache:
                return cache[num]

            result = fib_helper(num - 1) + fib_helper(num - 2)
            cache[num] = result

            return result

        return fib_helper(n - 1) + fib_helper(n - 2)
