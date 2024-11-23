# Given an array of strings strs, group all anagrams together into sublists.
# You may return the output in any order.

from collections import defaultdict
def groupAnagrams(strs):
    res = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        res[key].append(word)
    return list(res.values())

strs = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(strs))