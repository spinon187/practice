class Solution:
    def maxProduct(self, nums):
        fromLeft, fromRight = nums[:], nums[::-1]
        leftMax, rightMax = nums[0], nums[-1]
        for i in range(1, len(nums)):
            fromLeft[i] *= (fromLeft[i-1] or 1)
            fromRight[i] *= (fromRight[i-1] or 1)
            leftMax = max(leftMax, fromLeft[i])
            rightMax = max(rightMax, fromRight[i])
        return max(leftMax, rightMax)