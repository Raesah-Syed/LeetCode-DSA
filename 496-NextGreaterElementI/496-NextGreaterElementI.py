# Last updated: 6/7/2026, 6:43:26 PM
#Need to find the next greater element to the right of the element in nums2. The next greater element needs to be done only for the elements that are same in nums1. This means I need to only perform the operation for all values in nums1. 
#My approach: I loop through nums2 and check if the stack is not empty or top element in stack is not less than n(iterable of nums2) and pop the element when it is. After I pop, I make a dictionary with popped element and its next rgeater element
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
       s=[]
       d={}
       
       for n in nums2:
            
            while s and s[-1]<n: # check if stack is not empty and top element is less than n
                p=s.pop() #if top element is less then pop
                d[p]=n # add popped element in dict and the next greater element to its right is n
            
            s.append(n) # for every n we have the greater element

       return [d.get(no,-1) for no in nums1]







            