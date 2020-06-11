def groupAnagrams(self, strs):
    key = {}
    for s in strs:
        tag = tuple(sorted(s))
        if tag not in key:
            key[tag] = []
        key[tag].append(s)
    return key.values()