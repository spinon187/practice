class Solution:
    def mctFromLeafValues(self, arr):
        stack = [float('inf')]
        total = 0
        for num in arr:
            while stack and stack[-1] <= num:
                curr = stack.pop()
                total += curr * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            curr = stack.pop()
            total += curr * stack[-1]
        return total