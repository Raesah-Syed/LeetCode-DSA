# Last updated: 5/23/2026, 7:57:10 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}

        for s in strs:
            k="".join(sorted(s))
            if k in d:
                d[k].append(s)
            else:
                d[k] = [s]
        return list(d.values())