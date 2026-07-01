class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        stack = [] # pair : ind , height

        for ind , h in enumerate(heights):
            start = ind
            while stack and h < stack[-1][1]:
                last_i , last_h = stack.pop()
                start = last_i
                length = ind - last_i
                ans = max(ans  , length * last_h)

            stack.append((start , h))
    
        for i , h in stack:
            ans = max(ans , (len(heights) - i) * h)
        
        return ans