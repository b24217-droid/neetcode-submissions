class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # like we have to keep check for 0's
        # and also for negative number ??
        # NO we dont need that 
        # simplest solution i can come up with 

        total = 1
        cnt0 = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                cnt0 += 1
            

        if cnt0 > 1:
            return [0] * len(nums)

        res = []
        if cnt0 == 1:
            for num in nums:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)

        else:
            for num in nums:
                res.append(total // num)

        return res

        