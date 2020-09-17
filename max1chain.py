class Solution:
    def findMaxConsecutiveOnes(self, nums):
        current, running_max = 0, 0
        for x in nums:
            if x == 1:
                current += 1
                running_max = max(current, running_max)
            else:
                current = 0
        return running_max