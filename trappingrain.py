class Solution:
    def trap(self, height):
        if len(height) == 0:
            return 0
        localMins = [0]*len(height)
        localMax = 0
        for i in range(len(height)):
            localMax = max(localMax, height[i])
            localMins[i] = localMax - height[i]
        localMax = 0
        for i in reversed(range(len(height))):
            localMax = max(localMax, height[i])
            localMins[i] = min(localMins[i], localMax - height[i])
        return reduce(lambda x,y: x+y, localMins)