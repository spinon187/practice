class NumArray:

    def __init__(self, nums):
        if not len(nums):
            return
        self.runningSums = [0]*len(nums)
        self.runningSums[0] = nums[0]
        for i in range(1, len(nums)):
            self.runningSums[i] = self.runningSums[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i > 0:
            return self.runningSums[j] - self.runningSums[i-1]
        else:
            return self.runningSums[j]
