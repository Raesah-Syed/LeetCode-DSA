# Last updated: 5/28/2026, 9:24:07 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        s=[]

        for i in range(len(operations)):
 
            if operations[i].isdigit() or operations[i][0]=='-':
                s.append(operations[i])

            elif operations[i]=='C':
                s.pop()

            elif operations[i]=='D':
                s.append((int(s[-1])*2))

            else:
                s.append(int(s[-1]) + int(s[-2]))
                #print(s)
        return sum(list(map(int, s)))