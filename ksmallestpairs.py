class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not len(nums1) or not len(nums2):
            return []
        results = []
        from heapq import heappush, heappop
        m, n, visited = len(nums1), len(nums2), set()
        heap = [(nums1[0]+nums2[0], (0, 0))]
        for _ in range(min(k, (m*n))):
            val, (i, j) = heappop(heap)
            results.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heappush(heap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
        return results