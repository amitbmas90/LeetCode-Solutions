class Solution:
    def isHappy(self, n):
        """
        Very interesting problem.
        We only need to memorize all the visited numbers.
        If any number reappears we know we found a cycle. Return False.
        :type n: int
        :rtype: bool
        """
        def calculate(num):
            """
            calculate the sum of square of digits in num
            """
            return sum([int(digit) ** 2 for digit in list(str(num))])

        seen = set()
        num = n

        while True:
            if num in seen:
                return False
            if num == 1:
                return True
            seen.add(num)
            num = calculate(num)
