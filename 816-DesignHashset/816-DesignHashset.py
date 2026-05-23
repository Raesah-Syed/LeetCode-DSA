# Last updated: 5/23/2026, 5:53:11 PM
class MyHashSet:

    def __init__(self):
        # We pick a prime number for the number of buckets to distribute keys evenly
        self.num_buckets = 769
        # Create an array of empty lists to handle multiple keys hashing to the same index
        self.buckets = [[] for _ in range(self.num_buckets)]

    def _hash(self, key: int) -> int:
        # Custom internal hash function using modulo arithmetic
        return key % self.num_buckets

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # Prevent duplicate entries to maintain set properties
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        # Safely remove the element only if it exists in the calculated bucket
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        # Scan the tiny inner bucket array to see if the key is present
        return key in self.buckets[bucket_idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)