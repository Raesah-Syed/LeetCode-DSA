# Last updated: 5/18/2026, 7:49:17 PM
# sort the words to get same key for different strings and add to dictionary with list append
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        d={}
4
5        for s in strs:
6            k="".join(sorted(s))
7            if k in d:
8                d[k].append(s)
9            else:
10                d[k] = [s]
11        return list(d.values())