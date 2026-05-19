# Last updated: 5/19/2026, 5:37:16 PM
# Don't forget that the bucket may hold multiple key value pairs
1class MyHashMap:
2
3    def __init__(self):
4        self.num_buckets = 769
5        self.buckets = [[] for _ in range(self.num_buckets)]
6    
7    def _hash(self, key: int) -> int:
8        return key % self.num_buckets
9
10    def put(self, key: int, value: int) -> None:
11        bi = self._hash(key)
12        # Scan the bucket to see if the key already exists
13        for kv_pair in self.buckets[bi]:
14            if kv_pair[0] == key:
15                kv_pair[1] = value  # Update the existing value
16                return
17        # If it's a completely new key, append the pair
18        self.buckets[bi].append([key, value])
19
20    def get(self, key: int) -> int:
21        bi = self._hash(key)
22        # Scan the bucket to find the matching key
23        for kv_pair in self.buckets[bi]:
24            if kv_pair[0] == key:
25                return kv_pair[1]  # Return the value
26        return -1
27
28    def remove(self, key: int) -> None:
29        bi = self._hash(key)
30        # Iterate with an index to easily pop the pair out of the sub-list
31        for i, kv_pair in enumerate(self.buckets[bi]):
32            if kv_pair[0] == key:
33                self.buckets[bi].pop(i)
34                return