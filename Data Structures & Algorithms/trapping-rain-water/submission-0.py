class Solution:
    def trap(self, arr: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # i keep two pointers
        # every height is responsible i guess
        # so at each height see how you will update

        i = 0
        j = len(arr) - 1
        leftmax , rightmax = arr[i] , arr[j]
        ans = 0 
        while i < j:
            if leftmax <= rightmax:
                ans += max(0 , leftmax - arr[i])
                i += 1
                leftmax = max(arr[i], leftmax)
            else:
                ans += max(0 ,rightmax - arr[j])
                j -= 1
                rightmax = max(arr[j] , rightmax)
        
        return ans