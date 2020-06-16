class Solution:
    def minSubArrayLen(self, s, nums):
        length = float('inf')
        j = 0
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            while running >= s:
                length = min(length, i+1-j)
                running -= nums[j]
                j += 1
        return length if length != float('inf') else 0