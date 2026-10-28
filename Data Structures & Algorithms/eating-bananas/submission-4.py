class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        if h < len(piles):
            return False 


        while low < high:
            mid = (low + high) // 2 
            if self.checker(mid , piles , h):
                high = mid
            else:
                low = mid + 1 

        return high 

    def checker(self , rate , piles , h):
        time_taken = 0 
        for pile in piles:
            time_taken += pile // rate + (1 if pile % rate != 0 else 0)

        return time_taken <= h

     


        