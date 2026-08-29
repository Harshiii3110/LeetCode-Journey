from collections import defaultdict, OrderedDict


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0

        # key -> [value, frequency]
        self.cache = {}

        # frequency -> OrderedDict of keys
        # First = LRU, Last = MRU
        self.freq = defaultdict(OrderedDict)

        # Minimum frequency in the cache
        self.min_freq = 0

    def update_frequency(self, key):
        value, old_freq = self.cache[key]

        # Remove from old frequency
        del self.freq[old_freq][key]

        # If no keys remain at this frequency
        if not self.freq[old_freq]:
            del self.freq[old_freq]

            if self.min_freq == old_freq:
                self.min_freq += 1

        # Increase frequency
        new_freq = old_freq + 1
        self.cache[key] = [value, new_freq]

        # Add as most recently used
        self.freq[new_freq][key] = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        value = self.cache[key][0]

        # get increases frequency
        self.update_frequency(key)

        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if self.capacity == 0:
            return

        # Key already exists
        if key in self.cache:
            self.cache[key][0] = value

            # put also increases frequency
            self.update_frequency(key)
            return

        # Cache is full
        if self.size == self.capacity:

            # Get LFU frequency
            least_freq = self.min_freq

            # Remove LRU key among the LFU keys
            lru_key, _ = self.freq[least_freq].popitem(last=False)

            del self.cache[lru_key]
            self.size -= 1

        # Insert new key
        self.cache[key] = [value, 1]

        self.freq[1][key] = None

        # New key always has frequency 1
        self.min_freq = 1

        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
