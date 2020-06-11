def intersection(self, nums1, nums2):
    k = {}
    for n in nums1:
        k[n] = True
    output = []
    for n in nums2:
        if n in k and k[n] is True:
            output.append(n)
            k[n] = False
    return output