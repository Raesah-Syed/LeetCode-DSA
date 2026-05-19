# Last updated: 5/19/2026, 4:24:54 PM
# Relate this to building the linked list class and class node with constructor. Helps get an idea of how to build own data structrure
1class MyHashSet:
2
3    def __init__(self):
4        self.value=set()
5
6    def add(self, key: int) -> None:
7        self.value.add(key)
8
9    def remove(self, key: int) -> None:
10        if key in self.value:
11            self.value.remove(key)
12
13    def contains(self, key: int) -> bool:
14        if key in self.value:
15            return True
16        else:
17            return False
18
19
20# Your MyHashSet object will be instantiated and called as such:
21# obj = MyHashSet()
22# obj.add(key)
23# obj.remove(key)
24# param_3 = obj.contains(key)