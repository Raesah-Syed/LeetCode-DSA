# Last updated: 6/20/2026, 11:49:06 PM
class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        s=[timestamp,value]
        self.d[key].append(s)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.d:
            return ""
        
        pairs= self.d[key]

        if timestamp<pairs[0][0]:
            return ""

        left,right=0,len(pairs)-1

        while left<=right:
            mid=(left+right)//2

            if timestamp==pairs[mid][0]:
                return pairs[mid][1]
            
            elif timestamp<pairs[mid][0]:
                right=mid-1
            
            else:
                left=mid+1
        
        return pairs[right][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)