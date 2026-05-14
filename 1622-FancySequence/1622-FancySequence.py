# Last updated: 5/14/2026, 11:20:24 AM
1class Solution:
2    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
3        c=0
4        t=0
5        capacity.sort(reverse=True)
6        print(capacity)
7        for x in capacity:
8            if c>=sum(apple):
9                break
10            else:
11                c+=x
12                t+=1
13        return t