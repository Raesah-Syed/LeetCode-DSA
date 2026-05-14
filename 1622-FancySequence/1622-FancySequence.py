# Last updated: 5/14/2026, 11:24:50 AM
1class Solution:
2    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
3        c=0
4        t=0
5        sa=sum(apple)
6        capacity.sort(reverse=True)
7        print(capacity)
8        for x in capacity:
9            if c>=sa:
10                break
11            else:
12                c+=x
13                t+=1
14        return t