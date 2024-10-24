class RandomizedSet:

    def __init__(self):
        self.a= set()

    def insert(self, val: int) -> bool:
        if val in self.a:
            return False
        self.a.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.a:
            self.a.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if len(self.a)> 0:
            return random.choice(list(self.a))
        return -1


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()