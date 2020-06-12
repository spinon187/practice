class Solution:
    def rob(self, nums):
        if len(nums) < 2:
            return nums[0] if len(nums) else 0
        first = self.subRob(nums[:-1])
        last = self.subRob(nums[1:])
        return max(first, last)
        
        
    def subRob(self, arr):
        if len(arr) < 2:
            return arr[0] if len(arr) else 0
        running = [arr[0], max(arr[0], arr[1])]
        for i in range(2, len(arr)):
            running.append(max(running[i-1], running[i-2] + arr[i]))
        return running[-1]