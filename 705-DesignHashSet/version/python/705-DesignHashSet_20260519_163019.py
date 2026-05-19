# Last updated: 5/19/2026, 4:30:19 PM
1class MyHashSet:
2
3    def __init__(self):
4        # We pick a prime number for the number of buckets to distribute keys evenly
5        self.num_buckets = 769
6        # Create an array of empty lists to handle multiple keys hashing to the same index
7        self.buckets = [[] for _ in range(self.num_buckets)]
8
9    def _hash(self, key: int) -> int:
10        # Custom internal hash function using modulo arithmetic
11        return key % self.num_buckets
12
13    def add(self, key: int) -> None:
14        bucket_idx = self._hash(key)
15        # Prevent duplicate entries to maintain set properties
16        if key not in self.buckets[bucket_idx]:
17            self.buckets[bucket_idx].append(key)
18
19    def remove(self, key: int) -> None:
20        bucket_idx = self._hash(key)
21        # Safely remove the element only if it exists in the calculated bucket
22        if key in self.buckets[bucket_idx]:
23            self.buckets[bucket_idx].remove(key)
24
25    def contains(self, key: int) -> bool:
26        bucket_idx = self._hash(key)
27        # Scan the tiny inner bucket array to see if the key is present
28        return key in self.buckets[bucket_idx]
29
30
31# Your MyHashSet object will be instantiated and called as such:
32# obj = MyHashSet()
33# obj.add(key)
34# obj.remove(key)
35# param_3 = obj.contains(key)