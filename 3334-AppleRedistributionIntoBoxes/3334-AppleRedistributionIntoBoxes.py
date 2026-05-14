# Last updated: 5/14/2026, 11:21:02 AM
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        c=0
        t=0
        capacity.sort(reverse=True)
        print(capacity)
        for x in capacity:
            if c>=sum(apple):
                break
            else:
                c+=x
                t+=1
        return t