# Last updated: 6/7/2026, 4:48:35 PM
## I need to push all characters onto stack and only pop when there's a digit. The didgit must be popped with a non-digit character
class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for a in s:
            if a.isdigit() == False:
                st.append(a)
            if a.isdigit():
                st.pop()
        return("".join(st))