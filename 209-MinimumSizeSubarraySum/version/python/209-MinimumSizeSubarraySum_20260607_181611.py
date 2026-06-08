# Last updated: 6/7/2026, 6:16:11 PM
1#Need to find the next greater element to the right of the element in nums2. The next greater element needs to be done only for the elements that are same in nums1. This means I need to only perform the operation for all values in nums1. 
2#My approach: I loop through nums2 and check if the stack is not empty or top element in stack is not less than n(iterable of nums2) and pop the element when it is. After I pop, I make a dictionary with popped element and its next rgeater element
3class Solution:
4    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
5       
6       s=[]
7       d={}
8       
9       for n in nums2:
10            
11            while s and s[-1]<n: # check if stack is not empty and top element is less than n
12                p=s.pop() #if top element is less then pop
13                d[p]=n # add popped element in dict and the next greater element to its right is n
14            
15            s.append(n) # for every n we have the greater element
16
17       return [d.get(no,-1) for no in nums1]
18
19
20
21
22
23
24
25            