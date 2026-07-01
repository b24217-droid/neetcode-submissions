class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        n = len(position)
        for i in range(n):
            arr.append((position[i] , speed[i]))

        stack = [] # consists the time taken ??
        arr.sort(reverse = True)
        for i in range(n):
            time_taken = (target - arr[i][0]) / arr[i][1]
            stack.append(time_taken)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
    
        return len(stack)
