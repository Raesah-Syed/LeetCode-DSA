# Last updated: 6/7/2026, 4:48:20 PM
# Only append when element is character and pop when it is a digit. The question requires to return only a string with non-digit elements.
1## I need to push all characters onto stack and only pop when there's a digit. The didgit must be popped with a non-digit character
2class Solution:
3    def clearDigits(self, s: str) -> str:
4        st=[]
5        for a in s:
6            if a.isdigit() == False:
7                st.append(a)
8            if a.isdigit():
9                st.pop()
10        return("".join(st))