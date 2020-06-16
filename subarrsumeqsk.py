class Solution:
    def subarraySum(self, nums, k):
        dict = {}
        dict[0] = 1
        count = 0
        running = 0
        for num in nums:
            running += num
            if running - k in dict:
                count += dict[running - k]
            if running not in dict:
                dict[running] = 0
            dict[running] += 1
        return count