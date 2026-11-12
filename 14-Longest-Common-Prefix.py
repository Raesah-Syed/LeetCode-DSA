class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        x=strs[0]

        for i in range(len(x)):
            c=x[i]
            for s in strs[1:]:
                if i==len(s) or c!=s[i]:
                    return x[:i]
        return x
            

