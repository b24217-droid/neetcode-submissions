import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1

        max_k = max(piles) # O n
        min_k = 1
        ans = max_k

        # time take n < hours
        while min_k <= max_k:
            k = (min_k + max_k) // 2
            time_taken = self.checker(k , piles)
            if time_taken > h:
                min_k = k + 1
            else:
                max_k = k - 1
                ans = min(ans , k)
        
        return ans
                

    def checker(self, k , piles):
        time_taken = 0
        for pile in piles:
            time_taken += math.ceil(pile / k)
        
        return time_taken