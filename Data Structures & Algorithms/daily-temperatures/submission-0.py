class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # naive : O n ^ 2
        # simply using nested loops
        
        # better solution: 
        res = [0] * len(temp) 
        stack = [] # monotonic stack , keep track of the index (temp , ind)
        for i in range(len(temp)):
            t = temp[i]
            if not stack:
                stack.append((t , i))
            
            counter = 1
            while stack and t > stack[-1][0]:
                _ , ind = stack.pop()
                res[ind] = i - ind
                counter += 1
            
            stack.append((t , i))
        
        return res
    

