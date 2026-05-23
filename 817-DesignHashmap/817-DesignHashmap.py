# Last updated: 5/23/2026, 5:53:10 PM
class MyHashMap:

    def __init__(self):
        self.num_buckets = 769
        self.buckets = [[] for _ in range(self.num_buckets)]
    
    def _hash(self, key: int) -> int:
        return key % self.num_buckets

    def put(self, key: int, value: int) -> None:
        bi = self._hash(key)
        # Scan the bucket to see if the key already exists
        for kv_pair in self.buckets[bi]:
            if kv_pair[0] == key:
                kv_pair[1] = value  # Update the existing value
                return
        # If it's a completely new key, append the pair
        self.buckets[bi].append([key, value])

    def get(self, key: int) -> int:
        bi = self._hash(key)
        # Scan the bucket to find the matching key
        for kv_pair in self.buckets[bi]:
            if kv_pair[0] == key:
                return kv_pair[1]  # Return the value
        return -1

    def remove(self, key: int) -> None:
        bi = self._hash(key)
        # Iterate with an index to easily pop the pair out of the sub-list
        for i, kv_pair in enumerate(self.buckets[bi]):
            if kv_pair[0] == key:
                self.buckets[bi].pop(i)
                return