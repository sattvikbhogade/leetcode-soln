class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0 
        if n == 1:
            return 1  
        prior2 = 0
        prior1 = 1

        for i in range(2, n+1):
            curr = prior1 + prior2 
            prior2 = prior1
            prior1 = curr 
        return curr
