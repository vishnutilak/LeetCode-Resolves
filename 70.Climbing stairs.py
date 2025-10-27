class Solution:
    def climbStairs(self,n:int)->int:
        if n==1: return 1
        if n==2: return 2
        first, second = 1, 2

        for _ in range(3,n+1):
            third = first+second
            first, second = second, third
        return second