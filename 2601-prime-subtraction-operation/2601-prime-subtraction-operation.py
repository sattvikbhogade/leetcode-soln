class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # Step 1: Sieve of Eratosthenes
        MAX = 1000
        is_prime = [True] * (MAX + 1)

        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(MAX ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX + 1, i):
                    is_prime[j] = False

        # Step 2: Greedy
        prev = 0
        
        for num in nums:
            limit = num - prev 

            prime = 0 
            for p in range(limit-1, 1, -1):
                if is_prime[p]:
                    prime = p 
                    break 

            num -= prime 
            if num <= prev:
                return False 

            prev = num 

        return True
    