class Solution:
    def getTargetCopy(self, original, cloned, target):
        if not original:
            return None
        if original == target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)