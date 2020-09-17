class Solution:
    def findRestaurant(self, list1, list2):
        dict1 = {}
        for i, r in enumerate(list1):
            dict1[r] = i
        mindex = float('inf')
        current = []
        for i, r in enumerate(list2):
            if r in dict1:
                index_sum = i + dict1[r]
                if index_sum < mindex:
                    mindex = index_sum
                    current = [r]
                elif index_sum == mindex:
                    current.append(r)
        return current