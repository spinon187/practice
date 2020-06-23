class Solution:
    def pathInZigZagTree(self, label):
        if label == 1:
            return [1]
        level = 1
        while True:
            if 2**level - 1 >= label:
                break
            level += 1
        path = [label]
        level -= 1
        while level != 0:
            label = 2**(level-1) + ((2**(level+1) - 1 - label) // 2)
            path.append(label)
            level -= 1
        return reversed(path)