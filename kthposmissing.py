class Solution:
    def findKthPositive(self, arr, k):
        i = 0
        x = 1
        while k > 0:
            if i == len(arr):
                return x+k-1
            if arr[i] == x:
                x+=1
                i+=1
            else:
                k-=1
                x+=1
        return x-1