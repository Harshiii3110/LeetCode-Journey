class MyHashSet(object):

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        index = key % self.size
        bucket = self.buckets[index]

        for value in bucket:
            if value == key:
                return

        bucket.append(key)

    def remove(self, key):
        index = key % self.size
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    def contains(self, key):
        index = key % self.size
        bucket = self.buckets[index]

        for value in bucket:
            if value == key:
                return True

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
