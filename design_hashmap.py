class MyHashMap(object):

    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        index = key % self.size
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = key % self.size
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return -1

    def remove(self, key):
        index = key % self.size
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
