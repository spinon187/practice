class Solution:
    def duplicateZeros(self, arr):
        leftovers = deque()
        for i in range(len(arr)):
            if arr[i] == 0:
                leftovers.append(0)
            if len(leftovers):
                leftovers.append(arr[i])
                arr[i] = leftovers.popleft()