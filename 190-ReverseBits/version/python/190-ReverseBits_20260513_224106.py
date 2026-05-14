# Last updated: 5/13/2026, 10:41:06 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)[2:]
        if len(a) < 32:
            a = '0' * (32-len(a))+a
       # print(a)
        a = a[::-1]
       # print(a)
        a = int(a,2)
      #  print(a)
        
        return a