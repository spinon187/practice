class Solution:
    def sortedArrayToBST(self, nums):
        return self.sortHelper(nums, 0, len(nums))
        
    def sortHelper(self, nums, start, end):
        if start == end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        
        node.left = self.sortHelper(nums, start, mid)
        node.right = self.sortHelper(nums, mid+1, end)
        
        return node