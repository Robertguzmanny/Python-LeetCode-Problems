class Solution:
    # Define a class Solution with a method myPow to compute the power of a number.
    def myPow(self, x: float, n: int) -> float:
        # Function to compute x raised to the power of n.

        if n == 0:
            # If the exponent is 0, return 1.
            return 1

        elif n < 0:
            # If the exponent is negative, compute the reciprocal of x raised to the power of (-n - 1).
            # This is equivalent to 1 divided by (x raised to the power of -n - 1).
            return 1 / (x * self.myPow(x, -n -1))

        elif n % 2 == 0:
            # If the exponent is even, compute x raised to the power of n divided by 2.
            # This is done recursively to reduce the number of operations.
            a = self.myPow(x, n // 2)
            # Square the result to get x raised to the power of n.
            return a * a

        # If the exponent is odd, compute x times x raised to the power of n - 1.
        return x * self.myPow(x, n - 1)

test = Solution()
x = 2.34
n = 10
print(test.myPow(x,n))
