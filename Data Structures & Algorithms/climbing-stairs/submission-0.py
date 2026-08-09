class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n):
            temp = one
            one += two
            two = temp
        return two

    # 1 - 1
    # 2 - 2
    # 3 - 3
    # 4 - 5
    # 5 - 