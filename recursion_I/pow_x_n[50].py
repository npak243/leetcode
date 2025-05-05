class Solution:
    def myPow(self, x: float, n: int) -> float:

        def powHelper(x: float, n: int) -> float:
            if n < 2:
                return x ** n

            remain = n - (n // 2)
            return (x ** (n // 2)) * powHelper(x, remain)

        if n < 2:
            return x ** n

        remain = n - (n // 2)

        return (x ** (n // 2)) * powHelper(x, remain)
