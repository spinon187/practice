class Solution:
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return 0
        return self.recurse(nums, 0, len(nums)-1)
        
        
    def recurse(self, nums, start, end):
        if start > end:
            return None
        idx = start
        for n in range(start, end+1):
            if nums[n] > nums[idx]:
                idx = n
        root = TreeNode(nums[idx])
        root.left = self.recurse(nums, start, idx-1)
        root.right = self.recurse(nums, idx+1, end)
        return root