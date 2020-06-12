class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        j = len(nums) - 1
        while nums[i-1] >= nums[j]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        left = i
        right = len(nums) - 1
        while left < right:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
            right -= 1