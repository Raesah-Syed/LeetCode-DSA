# Last updated: 6/20/2026, 1:57:56 PM
1class TimeMap:
2
3    def __init__(self):
4        self.d={}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.d:
8            self.d[key]=[]
9        s=[timestamp,value]
10        self.d[key].append(s)
11
12    def get(self, key: str, timestamp: int) -> str:
13
14        if key not in self.d:
15            return ""
16        
17        pairs= self.d[key]
18
19        if timestamp<pairs[0][0]:
20            return ""
21
22        left,right=0,len(pairs)-1
23
24        while left<=right:
25            mid=(left+right)//2
26
27            if timestamp==pairs[mid][0]:
28                return pairs[mid][1]
29            
30            elif timestamp<pairs[mid][0]:
31                right=mid-1
32            
33            else:
34                left=mid+1
35        
36        return pairs[right][1]
37
38
39
40# Your TimeMap object will be instantiated and called as such:
41# obj = TimeMap()
42# obj.set(key,value,timestamp)
43# param_2 = obj.get(key,timestamp)